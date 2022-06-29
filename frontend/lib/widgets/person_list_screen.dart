import 'dart:convert';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:frontend/api/api_client.dart';

import '../constants.dart';
import '../models/person.dart';

class PersonListScreen extends StatefulWidget {
  const PersonListScreen({Key? key}) : super(key: key);

  @override
  _PersonListScreenState createState() => _PersonListScreenState();
}

class _PersonListScreenState extends State<PersonListScreen> {
  late final APIClient apiClient;

  Future<List<Person>>? _futurePersons;

  @override
  void initState() {
    super.initState();

    _initApiClient();
    _loadPersons();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: _onAddPressed,
      ),
      body: FutureBuilder<List<Person>>(
        future: _futurePersons,
        builder: (context, snapshot) {
          if (snapshot.hasData && snapshot.data != null) {
            var persons = snapshot.data!;
            return ListView(
              children: persons
                  .map((pers) => ListTile(
                        title: Text("${pers.first_name} ${pers.last_name}"),
                      ))
                  .toList(),
            );
          } else {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
    );
  }

  void _initApiClient() {
    var dio = Dio(BaseOptions());
    dio.options.contentType = "application/json";
    String basicAuth =
        'Basic ${base64.encode(utf8.encode('${Constants.adminUserName}:${Constants.adminPw}'))}';
    dio.options.headers["authorization"] = basicAuth;

    apiClient = APIClient(dio);
  }

  void _loadPersons() {
    _futurePersons = apiClient.getPersons();
  }

  void _onAddPressed() async {
    var firstName = "", lastName = "";
    await showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Neue Person'),
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(
                  decoration: InputDecoration(labelText: "Vorname"),
                  onChanged: (value) {
                    firstName = value;
                  },
                ),
                TextField(
                  decoration: InputDecoration(labelText: "Nachname"),
                  onChanged: (value) {
                    lastName = value;
                  },
                ),
              ],
            ),
            actions: [
              TextButton(
                  onPressed: () => Navigator.of(context).pop(),
                  child: Text("ok"))
            ],
          );
        });

    await apiClient
        .addNewPerson(
            Person(first_name: firstName, last_name: lastName, gender: 1))
        .catchError((Object obj) {
      final res = (obj as DioError).response;
      debugPrint(
          "Got error : ${res!.statusCode} -> ${res.statusMessage} :: ${res.data.toString()}");
    });

    setState(() {
      _loadPersons();
    });
  }
}

import 'package:dio/dio.dart';
import 'package:retrofit/http.dart';

import '../constants.dart';
import '../models/person.dart';

part 'api_client.g.dart';

@RestApi(baseUrl: Constants.apiBaseUrl)
abstract class APIClient {
  factory APIClient(Dio dio, {String baseUrl}) = _APIClient;

  @GET("/persons")
  Future<List<Person>> getPersons();

  @POST("/persons/")
  Future addNewPerson(@Body() Person person);
}

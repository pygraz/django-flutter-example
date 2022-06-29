import 'package:json_annotation/json_annotation.dart';

part 'person.g.dart';

@JsonSerializable()
class Person {
  num? id;
  String? first_name;
  String? last_name;
  num? gender;
  String? date_of_birth;

  Person(
      {this.id,
      this.first_name,
      this.last_name,
      this.gender,
      this.date_of_birth});

  factory Person.fromJson(Map<String, dynamic> json) => _$PersonFromJson(json);

  Map<String, dynamic> toJson() => _$PersonToJson(this);
}

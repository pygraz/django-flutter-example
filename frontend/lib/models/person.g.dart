// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'person.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Person _$PersonFromJson(Map<String, dynamic> json) => Person(
      id: json['id'] as num?,
      first_name: json['first_name'] as String?,
      last_name: json['last_name'] as String?,
      gender: json['gender'] as num?,
      date_of_birth: json['date_of_birth'] as String?,
    );

Map<String, dynamic> _$PersonToJson(Person instance) => <String, dynamic>{
      'id': instance.id,
      'first_name': instance.first_name,
      'last_name': instance.last_name,
      'gender': instance.gender,
      'date_of_birth': instance.date_of_birth,
    };

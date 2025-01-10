import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class AuthService {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();

  final String apiUrl = 'http://localhost:5000';

  // Stocker le token dans le stockage sécurisé
  Future<void> saveToken(String token) async {
    await _storage.write(key: 'auth_token', value: token);
  }

  // Méthode de connexion
  Future<Map<String, dynamic>?> login(String email, String password) async {
    try {
      // Requête POST vers l'API
      final response = await http.post(
        Uri.parse('$apiUrl/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        String token = data['token'];
        await saveToken(token); // Sauvegarder le token
        return data['user'];
      } else {
        print('Erreur de connexion : ${response.body}');
        return null;
      }
    } catch (e) {
      print('Exception pendant la connexion : $e');
      return null;
    }
  }

  static String hashPassword(String password) {
    final bytes = utf8.encode(password);
    final digest = sha256.convert(bytes);
    return digest.toString();
  }
}

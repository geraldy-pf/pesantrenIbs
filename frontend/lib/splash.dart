import 'package:flutter/material.dart';
import 'splash2.dart'; // pastikan file ini ada dan berisi class LoginPage

class SplashPage1 extends StatefulWidget {
  const SplashPage1({Key? key}) : super(key: key);

  @override
  State<SplashPage1> createState() => _SplashPage1State();
}

class _SplashPage1State extends State<SplashPage1> {
  double _opacity = 1.0;

  @override
  void initState() {
    super.initState();

    // Fade out logo setelah 2 detik
    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        _opacity = 0.0;
      });
    });

    // Pindah ke SplashPage2 setelah 3 detik
    Future.delayed(const Duration(seconds: 3), () {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (_) => const SplashPage2()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;

    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: AnimatedOpacity(
          opacity: _opacity,
          duration: const Duration(seconds: 1),
          child: Image.asset(
            'assets/img/logo.png',
            width: screenWidth * 0.895,
            fit: BoxFit.contain,
          ),
        ),
      ),
    );
  }
}
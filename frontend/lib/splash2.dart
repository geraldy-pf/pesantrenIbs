import 'package:flutter/material.dart';
import 'login.dart';

class SplashPage2 extends StatelessWidget {
  const SplashPage2({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    double screenHeight = MediaQuery.of(context).size.height;

    double bgHeight =
        screenHeight * (331 / 844);
    double paddingTop = screenHeight * (30 / 844);
    double paddingSide = screenWidth * (20 / 390);

    return Scaffold(
      body: Stack(
        children: [
          Container(
            width: screenWidth,
            height: bgHeight,
            color: const Color(0xFF288DE5), // hex #288DE5
          ),

          Positioned(
            top: 0,
            left: 0,
            right: 0,
            child: Image.asset(
              'assets/img/bg_splash.png',
              width: screenWidth,
              height: bgHeight,
              fit: BoxFit.cover,
            ),
          ),

          SafeArea(
            child: Padding(
              padding: EdgeInsets.only(
                top: paddingTop,
                left: paddingSide,
                right: paddingSide,
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Image.asset(
                    'assets/img/logo.png',
                    width: 101,
                    height: 44,
                  ),

                  GestureDetector(
                    onTap: () {
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(builder: (_) => const LoginPage()),
                      );
                    },
                    child: const Text(
                      "Lewati",
                      style: TextStyle(
                        fontSize: 12,
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

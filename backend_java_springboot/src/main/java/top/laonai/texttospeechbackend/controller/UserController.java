package top.laonai.texttospeechbackend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import top.laonai.texttospeechbackend.service.UserService;

import java.util.Map;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api")
public class UserController {

    @Autowired
    private UserService userService;

    // 用户注册接口
    @PostMapping("/register")
    public ResponseEntity<?> registerUser(@RequestBody Map<String, String> data) {
        String username = data.get("username");
        String password = data.get("password");

        Map<String, Object> result = userService.registerUser(username, password);
        if (result.containsKey("error")) {
            return ResponseEntity.badRequest().body(result);
        }

        return ResponseEntity.ok(result);
    }

    // 用户登录接口
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody Map<String, String> loginData) {
        String username = loginData.get("username");
        String password = loginData.get("password");

        Map<String, Object> result = userService.login(username, password);
        if (result.containsKey("error")) {
            return ResponseEntity.status(401).body(result);
        }

        return ResponseEntity.ok(result);
    }


    @GetMapping("/test")
    public ResponseEntity<String> test() {
        return ResponseEntity.ok("Hello World");
    }
}

package top.laonai.texttospeechbackend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCrypt;
import org.springframework.stereotype.Service;
import org.springframework.dao.DataIntegrityViolationException;
import top.laonai.texttospeechbackend.module.UserInfo;
import top.laonai.texttospeechbackend.repository.UserInfoRepository;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserInfoRepository userInfoRepository;

    // 用户注册逻辑
    public Map<String, Object> registerUser(String username, String password) {
        Map<String, Object> response = new HashMap<>();

        if (isEmpty(username) || isEmpty(password)) {
            response.put("error", "用户名和密码是必需的");
            return response;
        }

        // 检查用户是否已存在
        if (userInfoRepository.findByUsername(username).isPresent()) {
            response.put("error", "用户已存在");
            return response;
        }

        // 创建新用户
        UserInfo newUser = new UserInfo();
        newUser.setUsername(username);

        // 哈希化密码
        String hashedPassword = BCrypt.hashpw(password, BCrypt.gensalt());
        newUser.setPassword(hashedPassword);

        try {
            userInfoRepository.save(newUser);
            response.put("message", "注册成功");
        } catch (DataIntegrityViolationException e) {
            response.put("error", "注册失败: 用户名可能已存在");
        } catch (Exception e) {
            response.put("error", "注册失败: " + e.getMessage());
        }

        return response;
    }

    // 用户登录逻辑
    public Map<String, Object> login(String username, String password) {
        Map<String, Object> response = new HashMap<>();

        if (isEmpty(username) || isEmpty(password)) {
            response.put("error", "用户名和密码是必需的");
            return response;
        }

        // 查询用户信息
        Optional<UserInfo> userOptional = userInfoRepository.findByUsername(username);
        if (userOptional.isEmpty()) {
            response.put("error", "用户名或密码不正确");
            return response;
        }

        UserInfo user = userOptional.get();

        // 验证密码
        if (BCrypt.checkpw(password, user.getPassword())) {
            response.put("message", "登录成功");
        } else {
            response.put("error", "用户名或密码不正确");
        }

        return response;
    }

    // 判断字符串是否为空
    private boolean isEmpty(String value) {
        return value == null || value.trim().isEmpty();
    }
}

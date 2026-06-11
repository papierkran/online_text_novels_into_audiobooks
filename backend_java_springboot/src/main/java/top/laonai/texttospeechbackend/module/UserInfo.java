package top.laonai.texttospeechbackend.module;


import jakarta.persistence.*;
import org.springframework.security.crypto.bcrypt.BCrypt;

@Entity
@Table(name = "user_info")
public class UserInfo {

@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;

@Column(name = "username", nullable = false, unique = true)
private String username;

@Column(name = "password", nullable = false)
private String password;

// 设置密码时进行哈希
public void setPassword(String password) {
this.password = BCrypt.hashpw(password, BCrypt.gensalt());
}

// 检查密码是否正确
public boolean checkPassword(String plainPassword) {
return BCrypt.checkpw(plainPassword, this.password);
}

// Getters 和 Setters
public Long getId() {
return id;
}

public void setId(Long id) {
this.id = id;
}

public String getUsername() {
return username;
}

public void setUsername(String username) {
this.username = username;
}

public String getPassword() {
return password;
}
}

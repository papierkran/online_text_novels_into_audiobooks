package top.laonai.texttospeechbackend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import top.laonai.texttospeechbackend.module.UserInfo;

import java.util.Optional;

public interface UserInfoRepository extends JpaRepository<UserInfo, Long> {
    Optional<UserInfo> findByUsername(String username);
}

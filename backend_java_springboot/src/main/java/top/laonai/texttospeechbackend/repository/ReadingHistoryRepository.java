package top.laonai.texttospeechbackend.repository;


import top.laonai.texttospeechbackend.module.ReadingHistory;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ReadingHistoryRepository extends JpaRepository<ReadingHistory, Long> {

    // 根据 userId 查询所有阅读历史记录
    List<ReadingHistory> findByUserId(Long userId);

    // 查询用户最近的一条阅读记录，按 readTime 降序排序
    ReadingHistory findTopByUserIdOrderByReadTimeDesc(Long userId);
}

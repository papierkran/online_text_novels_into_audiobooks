package top.laonai.texttospeechbackend.service;

import top.laonai.texttospeechbackend.module.NovelsInfo;
import top.laonai.texttospeechbackend.module.ReadingHistory;
import top.laonai.texttospeechbackend.module.UserInfo;
import top.laonai.texttospeechbackend.repository.NovelsInfoRepository;
import top.laonai.texttospeechbackend.repository.ReadingHistoryRepository;
import top.laonai.texttospeechbackend.repository.UserInfoRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class ReadingHistoryService {

    @Autowired
    private ReadingHistoryRepository readingHistoryRepository;

    @Autowired
    private UserInfoRepository userInfoRepository;  // 注入 UserRepository

    @Autowired
    private NovelsInfoRepository novelsInfoRepository;  // 注入 NovelsInfoRepository

    // 保存阅读历史记录
    public Map<String, String> saveReadingHistory(Long userId, Long novelId, String content) {
        try {
            // 创建新的阅读历史记录
            ReadingHistory newHistory = new ReadingHistory();

            // 从数据库中获取 User 和 NovelsInfo 对象（假设这两个对象已存在）
            UserInfo user = userInfoRepository.findById(userId)
                    .orElseThrow(() -> new RuntimeException("User not found"));
            NovelsInfo novel = novelsInfoRepository.findById(novelId.intValue())
                    .orElseThrow(() -> new RuntimeException("Novel not found"));

            // 设置关联对象
            newHistory.setUser(user);
            newHistory.setNovel(novel);
            newHistory.setReadContent(content);
            newHistory.setReadTime(LocalDateTime.now());  // 使用当前时间

            // 保存到数据库
            readingHistoryRepository.save(newHistory);
            return Map.of("message", "阅读历史记录已保存");
        } catch (Exception e) {
            return Map.of("error", e.getMessage());
        }
    }


    // 查询用户最近的阅读历史记录
    public Map<String, Object> getRecentReadingHistory(Long userId) {
        try {
            // 查询最近一条历史记录
            ReadingHistory recentHistory = readingHistoryRepository.findTopByUserIdOrderByReadTimeDesc(userId);
            if (recentHistory == null) {
                return Map.of("message", "No reading history found.");
            }

            return Map.of(
                    "id", recentHistory.getId(),
                    "novel_title", recentHistory.getNovel().getTitle(),
                    "read_content", recentHistory.getReadContent(),
                    "read_time", recentHistory.getReadTime()
            );
        } catch (Exception e) {
            return Map.of("error", e.getMessage());
        }
    }
}

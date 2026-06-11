package top.laonai.texttospeechbackend.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import top.laonai.texttospeechbackend.DTO.ReadingHistoryDto;
import top.laonai.texttospeechbackend.module.ReadingHistory;
import top.laonai.texttospeechbackend.repository.ReadingHistoryRepository;
import top.laonai.texttospeechbackend.service.ReadingHistoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api")
public class ReadingHistoryController {

    @Autowired
    private ReadingHistoryService readingHistoryService;

    // 保存阅读历史记录
    @PostMapping("/save_reading_history")
    public Map<String, String> saveReadingHistory(@RequestParam Long userId, @RequestParam Long novelId, @RequestParam String content) {
        return readingHistoryService.saveReadingHistory(userId, novelId, content);
    }

    // 查询用户的所有阅读历史记录
    @Autowired
    private ReadingHistoryRepository readingHistoryRepository;
    @GetMapping("/get_reading_history/{userId}")
    public ResponseEntity<List<ReadingHistoryDto>> getReadingHistory(@PathVariable("userId") Long userId) {
            List<ReadingHistory> histories = readingHistoryRepository.findByUserId(userId);
            List<ReadingHistoryDto> historyDtos = histories.stream()
                    .map(ReadingHistoryDto::new)
                    .collect(Collectors.toList());
            return ResponseEntity.ok(historyDtos);
    }

    // 查询用户最近的阅读历史记录
    @GetMapping("/get_recent_reading_history/{userId}")
    public Map<String, Object> getRecentReadingHistory(@PathVariable Long userId) {
        return readingHistoryService.getRecentReadingHistory(userId);
    }
}

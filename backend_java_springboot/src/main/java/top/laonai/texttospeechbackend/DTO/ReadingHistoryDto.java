package top.laonai.texttospeechbackend.DTO;

import top.laonai.texttospeechbackend.module.ReadingHistory;

import java.time.LocalDateTime;

import com.fasterxml.jackson.annotation.JsonProperty;

public class ReadingHistoryDto {
    private Long id;

    @JsonProperty("user_id") // 将 userId 改为 user_id
    private Long userId;

    @JsonProperty("novel_title") // 将 novelTitle 改为 novel_title
    private String novelTitle;

    @JsonProperty("read_content")
    private String readContent;

    @JsonProperty("read_time")
    private LocalDateTime readTime;

    public ReadingHistoryDto(ReadingHistory history) {
        this.id = history.getId();
        if (history.getUser() != null) {
            this.userId = history.getUser().getId();
        }
        if (history.getNovel() != null) {
            this.novelTitle = history.getNovel().getTitle();
        }
        this.readContent = history.getReadContent();
        this.readTime = history.getReadTime();
    }

    // Getter 和 Setter 方法
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public String getNovelTitle() {
        return novelTitle;
    }

    public void setNovelTitle(String novelTitle) {
        this.novelTitle = novelTitle;
    }

    public String getReadContent() {
        return readContent;
    }

    public void setReadContent(String readContent) {
        this.readContent = readContent;
    }

    public LocalDateTime getReadTime() {
        return readTime;
    }

    public void setReadTime(LocalDateTime readTime) {
        this.readTime = readTime;
    }
}
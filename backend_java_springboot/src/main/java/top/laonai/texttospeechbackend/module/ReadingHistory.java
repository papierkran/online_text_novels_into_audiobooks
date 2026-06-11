package top.laonai.texttospeechbackend.module;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "reading_history")
public class ReadingHistory {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)  // 使用延迟加载，避免不必要的数据库查询
    @JoinColumn(name = "user_id", nullable = false)
    private UserInfo user;

    @ManyToOne(fetch = FetchType.LAZY)  // 根据需求选择EAGER或者LAZY
    @JoinColumn(name = "novel_id", nullable = false)
    private NovelsInfo novel;

    @Column(name = "read_time", columnDefinition = "DATETIME")
    private LocalDateTime readTime;

    @Column(name = "read_content", columnDefinition = "TEXT", nullable = false)
    private String readContent;

    // 默认构造函数
    public ReadingHistory() {
    }

    public ReadingHistory(UserInfo user, NovelsInfo novel, String readContent, LocalDateTime readTime) {
        this.user = user;
        this.novel = novel;
        this.readContent = readContent;
        this.readTime = readTime;
    }

    // Getter 和 Setter 方法

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public UserInfo getUser() {  // 修改返回类型为 User
        return user;
    }

    public void setUser(UserInfo user) {  // 修改参数类型为 User
        this.user = user;
    }

    public NovelsInfo getNovel() {
        return novel;
    }

    public void setNovel(NovelsInfo novel) {
        this.novel = novel;
    }

    public LocalDateTime getReadTime() {
        return readTime;
    }

    public void setReadTime(LocalDateTime readTime) {
        this.readTime = readTime;
    }

    public String getReadContent() {
        return readContent;
    }

    public void setReadContent(String readContent) {
        this.readContent = readContent;
    }
}

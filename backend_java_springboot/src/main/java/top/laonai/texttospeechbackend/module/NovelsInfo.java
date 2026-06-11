package top.laonai.texttospeechbackend.module;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;

// 标注为JPA实体类
@Entity
@Table(name = "novels_info")
public class NovelsInfo {

    // 主键ID
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // 标题字段
    @Column(name = "title", nullable = false, length = 255)
    private String title;

    // 链接字段
    @Column(name = "url", nullable = true, length = 255)
    private String url;

    // 内容字段
    @Column(name = "content", nullable = false, columnDefinition = "TEXT")
    private String content;

    // 保存路径字段
    @JsonProperty("file_path")
    @Column(name = "file_path", nullable = true, length = 255)
    private String filePath;


    // 封面链接字段
    @JsonProperty("cover_url")
    @Column(name = "cover_url", nullable = true, length = 255)
    private String coverUrl;

    // 无参构造函数（JPA要求）
    public NovelsInfo() {}

    // 带参构造函数
    public NovelsInfo(String title, String url, String content, String filePath, String coverUrl) {
        this.title = title;
        this.url = url;
        this.content = content;
        this.filePath = filePath;
        this.coverUrl = coverUrl;
    }

    // Getter 和 Setter 方法
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public String getCoverUrl() {
        return coverUrl;
    }

    public void setCoverUrl(String coverUrl) {
        this.coverUrl = coverUrl;
    }
}

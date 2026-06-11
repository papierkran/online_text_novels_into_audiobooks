package top.laonai.texttospeechbackend.controller;

import org.springframework.http.ResponseEntity;
import top.laonai.texttospeechbackend.DTO.WordCountResponse;
import top.laonai.texttospeechbackend.module.NovelsInfo;
import top.laonai.texttospeechbackend.service.NovelsInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class NovelsInfoController {

    @Autowired
    private NovelsInfoService novelsInfoService;

    // 获取所有小说
    @GetMapping("/get_all_novels")
    public List<NovelsInfo> getAllNovels(NovelsInfo novelsInfo) {
        return novelsInfoService.getAllNovels();
    }

    // 根据ID获取小说
    @GetMapping("/get_novel_id/{id}")
    public NovelsInfo getNovelById(@PathVariable Long id) {
        return novelsInfoService.getNovelById(id);
    }

    // 添加小说
    @PostMapping("/add_novel")
    public NovelsInfo addNovel(@RequestBody NovelsInfo novel) {
        return novelsInfoService.addNovel(novel);
    }

    // 更新小说
    @PutMapping("/update_novel/{id}")
    public NovelsInfo updateNovel(@PathVariable Long id, @RequestBody NovelsInfo novelDetails) {
        return novelsInfoService.updateNovel(id, novelDetails);
    }

    // 删除小说
    @DeleteMapping("/delete_novel/{id}")
    public void deleteNovel(@PathVariable Long id) {
        novelsInfoService.deleteNovel(id);
    }

    // 根据标题获取小说内容
    @GetMapping("/get_all_novels/{title}")
    public ResponseEntity<?> getNovelContent(@PathVariable String title) {
        try {
            NovelsInfo novel = novelsInfoService.getNovelByTitle(title);
            if (novel != null) {

                return ResponseEntity.ok().body(new NovelContentResponse(novel.getContent()));  // 返回小说内容
            } else {
                return ResponseEntity.status(404).body("Novel not found");
            }
        } catch (Exception e) {
            return ResponseEntity.status(500).body("Error: " + e.getMessage());
        }
    }

    // 统计小说总字数的 REST API 端点
    @GetMapping("/count_words")
    public WordCountResponse countWords() {
        int totalWordCount = novelsInfoService.countWordsInNovels();
        return new WordCountResponse(totalWordCount);
    }

    // 定义一个响应类
    static class NovelContentResponse {
        private String content;

        public NovelContentResponse(String content) {
            this.content = content;
        }

        public String getContent() {
            return content;
        }

        public void setContent(String content) {
            this.content = content;
        }
    }
}

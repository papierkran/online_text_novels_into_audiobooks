package top.laonai.texttospeechbackend.service;

import top.laonai.texttospeechbackend.module.NovelsInfo;
import top.laonai.texttospeechbackend.repository.NovelsInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NovelsInfoService {

    @Autowired
    private NovelsInfoRepository novelsInfoRepository;

    // 获取所有小说
    public List<NovelsInfo> getAllNovels() {
        return novelsInfoRepository.findAll();  // 返回 List<NovelsInfo>
    }

    // 根据 ID 获取小说
    public NovelsInfo getNovelById(Long id) {
        return novelsInfoRepository.findById(id);
    }
    // 添加小说
    public NovelsInfo addNovel(NovelsInfo novel) {
        return novelsInfoRepository.save(novel);
    }

    // 更新小说
    public NovelsInfo updateNovel(Long id, NovelsInfo novelDetails) {
        NovelsInfo novel = novelsInfoRepository.findById(id);

        // 更新小说信息
        novel.setTitle(novelDetails.getTitle());
        novel.setUrl(novelDetails.getUrl());
        novel.setContent(novelDetails.getContent());
        novel.setFilePath(novelDetails.getFilePath());
        novel.setCoverUrl(novelDetails.getCoverUrl());

        // 保存更新后的小说信息
        return novelsInfoRepository.save(novel);
    }

    // 删除小说
    public void deleteNovel(Long id) {
        NovelsInfo novel = novelsInfoRepository.findById(id);
        novelsInfoRepository.delete(novel);
    }

    // 根据标题获取小说
    public NovelsInfo getNovelByTitle(String title) {
        return novelsInfoRepository.findByTitle(title);  // 查找标题匹配的小说
    }


    // 计算所有小说的总字数
    public int countWordsInNovels() {
        try {
            // 查询所有已转换为有声小说的小说
            List<NovelsInfo> novels = novelsInfoRepository.findAll();

            int totalWordCount = 0;
            // 计算所有小说的总字数
            for (NovelsInfo novel : novels) {
                if (novel.getContent() != null && !novel.getContent().isEmpty()) { // 确保内容不为空
                    totalWordCount += novel.getContent().length(); // 获取内容的长度
                }
            }
            System.out.println("Total word count: " + totalWordCount);
            return totalWordCount;
        } catch (Exception e) {
            // 捕捉并抛出错误
            throw new RuntimeException("Error counting words: " + e.getMessage(), e);
        }
    }
}

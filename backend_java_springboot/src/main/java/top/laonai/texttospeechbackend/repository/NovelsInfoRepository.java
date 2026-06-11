package top.laonai.texttospeechbackend.repository;


import top.laonai.texttospeechbackend.module.NovelsInfo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NovelsInfoRepository extends JpaRepository<NovelsInfo, Integer> {
    // 额外的查询方法可以在这里定义，比如通过标题查找小说
    NovelsInfo findByTitle(String title);
    NovelsInfo findById(Long id);
}


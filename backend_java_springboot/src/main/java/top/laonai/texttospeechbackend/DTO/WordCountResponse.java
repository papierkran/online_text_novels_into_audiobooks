package top.laonai.texttospeechbackend.DTO;

import com.fasterxml.jackson.annotation.JsonProperty;

public class WordCountResponse {
    @JsonProperty("total_word_count")
    private int totalWordCount;

    public WordCountResponse(int totalWordCount) {
        this.totalWordCount = totalWordCount;
    }

    public int getTotalWordCount() {
        return totalWordCount;
    }

    public void setTotalWordCount(int totalWordCount) {
        this.totalWordCount = totalWordCount;
    }
}
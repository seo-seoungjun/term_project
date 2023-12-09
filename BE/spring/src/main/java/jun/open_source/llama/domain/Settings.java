package hoon.capstone.llama.domain;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class Settings {
    private Grammar grammar;
    private Integer maxTokens;
    private Double temperature;
    private Integer numberMessages;
    private Double presencePenalty;
    private Double frequencyPenalty;
}
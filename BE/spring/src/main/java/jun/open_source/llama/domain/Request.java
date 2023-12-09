package hoon.capstone.llama.domain;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import org.springframework.web.multipart.MultipartFile;

@Getter
public class Request {
    @NotNull
    private final MultipartFile file;

    @NotNull
    private final Grammar grammar;

    @NotNull
    @Min(128) @Max(8192)
    private final Integer maxTokens;

    @NotNull
    @Min(0) @Max(1)
    private final Double temperature;

    @NotNull
    @Min(1) @Max(10)
    private final Integer numberMessages;

    @NotNull
    @Min(-2) @Max(2)
    private final Double presencePenalty;

    @NotNull
    @Min(-2) @Max(2)
    private final Double frequencyPenalty;

    @NotNull
    private final String userMessage;

    public Request(MultipartFile file, Grammar grammar, Integer maxTokens, Double temperature,
                   Integer numberMessages, Double presencePenalty, Double frequencyPenalty,
                   String userMessage) {
        this.file = file;
        this.grammar = grammar;
        this.maxTokens = maxTokens;
        this.temperature = temperature;
        this.numberMessages = numberMessages;
        this.presencePenalty = presencePenalty;
        this.frequencyPenalty = frequencyPenalty;
        this.userMessage = userMessage;
    }
}


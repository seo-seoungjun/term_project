package hoon.capstone.llama.controller;

import hoon.capstone.llama.domain.Request;
import hoon.capstone.llama.domain.Settings;
import hoon.capstone.llama.service.RequestService;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@Tag(name = "Request", description = "flask에 request")
@RestController
public class RequestController {
    private final RequestService requestService;

    @Value("${flask.app.url}")
    private String URL;

    public RequestController(RequestService requestService) {
        this.requestService = requestService;
    }

    @PostMapping("/send")
    public String sendDataToFlask(@ModelAttribute Request request) {
        System.out.println(request);
        Settings settings = new Settings(request.getGrammar(), request.getMaxTokens(),
                request.getTemperature(), request.getNumberMessages(),
                request.getPresencePenalty(), request.getFrequencyPenalty());
        try {
            return requestService.sendFileAndData(request.getFile(), settings, request.getUserMessage(), URL);
        } catch (IOException e) {
            return "Error: " + e.getMessage();
        }
    }
}

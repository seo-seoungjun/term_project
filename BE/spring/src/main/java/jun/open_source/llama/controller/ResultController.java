package hoon.capstone.llama.controller;

import hoon.capstone.llama.domain.Result;
import hoon.capstone.llama.service.ResultService;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.CompletableFuture;


@Tag(name = "fetch", description = "결과 가져오기(비동기)")
@RestController
public class ResultController {

    private final ResultService resultService;

    public ResultController(ResultService resultService) {
        this.resultService = resultService;
    }

    @GetMapping("/summarizer")
    public CompletableFuture<ResponseEntity<?>> summarizer(@RequestBody Result response) {
        return resultService.processResult(response)
                .thenApply(ResponseEntity::ok);
    }

    @GetMapping("/goal_explorer")
    public CompletableFuture<ResponseEntity<?>> goalExplorer(@RequestBody Result response) {
        return resultService.processResult(response)
                .thenApply(ResponseEntity::ok);
    }

    @GetMapping("/visualization")
    public CompletableFuture<ResponseEntity<?>> visualization(@RequestBody Result response) {
        return resultService.processResult(response)
                .thenApply(ResponseEntity::ok);
    }
}

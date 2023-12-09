package hoon.capstone.llama.service;

import hoon.capstone.llama.domain.Result;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.util.concurrent.CompletableFuture;

@Service
public class ResultService {
    @Async
    public CompletableFuture<Result> processResult(Result result) {
        System.out.println("Processing result: " + result.getResult());
        return CompletableFuture.completedFuture(result);
    }
}

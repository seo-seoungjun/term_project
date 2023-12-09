package hoon.capstone.llama.config;

import hoon.capstone.llama.domain.Settings;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class FileConfig {
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}

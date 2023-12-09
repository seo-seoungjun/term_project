package hoon.capstone.llama.domain;

import lombok.Getter;

@Getter
public enum Grammar {
    SEABORN("Seaborn"),
    ALTAIR("Altair"),
    MATPLOTLIB("MatPlotLib"),
    GGPLOT("GGPlot");

    private final String library;

    Grammar(String library) {
        this.library = library;
    }

}

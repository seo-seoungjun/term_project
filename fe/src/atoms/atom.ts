import { atom } from 'recoil';

export enum Grammar {
  'Seaborn' = 'SEABORN',
  'Altair' = 'ALTAIR',
  'MatPlotlib' = 'MATPLOTLIB',
  'GGPlot' = 'GGPLOT',
}

export interface PostFileFormDataBody {
  [key: string]: any;
}

export interface ISettings {
  grammar: Grammar;
  max_tokens: string;
  temperature: string;
  number_messages: string;
  presence_penalty: string;
  frequency_penalty: string;
  user_message?: string;
  file: any;
}

interface IgenerateSettingsMinMaxValue {
  maxToken: {
    min: number;
    max: number;
  };
  temperature: {
    min: number;
    max: number;
  };
  numberMessages: {
    min: number;
    max: number;
  };
  presencePenalty: {
    min: number;
    max: number;
  };
  frequencyPenalty: {
    min: number;
    max: number;
  };
}

interface ImageContent {
  image_file: {
    file_id: string;
  };
  type: string;
}

interface TextContent {
  text: {
    annotations: any;
    value: string;
  };
  type: string;
}

export interface IVisualizationData {
  id: string;
  assistant_id: string;
  content: any;
  created_at: number;
  file_ids: any;
  metadata: any;
  object: string;
  role: string;
  run_id: string;
  thread_id: string;
}

export const grammarSettings = atom({
  key: 'grammerList',
  default: [
    Grammar.Seaborn,
    Grammar.Altair,
    Grammar.MatPlotlib,
    Grammar.GGPlot,
  ],
});

export const fileUpLoadSettings = atom<ISettings>({
  key: 'fileUpLoadSettings',
  default: {
    grammar: Grammar.Seaborn,
    max_tokens: '6336',
    temperature: '0',
    number_messages: '1',
    presence_penalty: '-2',
    frequency_penalty: '-2',
    user_message: '',
    file: null,
  },
  dangerouslyAllowMutability: true,
});

export const generateSettingsMinMaxValue = atom<IgenerateSettingsMinMaxValue>({
  key: 'generateSettingsMinMaxValue',
  default: {
    maxToken: {
      min: 128,
      max: 8192,
    },
    temperature: {
      min: 0,
      max: 1,
    },
    numberMessages: {
      min: -2,
      max: 10,
    },
    presencePenalty: {
      min: -2,
      max: 2,
    },
    frequencyPenalty: {
      min: -2,
      max: 2,
    },
  },
});

export const resultDatas = atom({
  key: 'resultData',
  default: [],
});

export const isDataExist = atom({
  key: 'isExist',
  default: false,
});

export const visualizationDatas = atom<IVisualizationData[]>({
  key: 'visualizationDatas',
  default: [],
});

class N_GRAMS:
    def __init__(self) -> None:
        self.word_mappings = {}
        self.bigram = {}
        self.load_sentences()

    def load_sentences(self):
        
        for line in open("sentences.txt"):
            line = line.strip()
            line_words = line.split(" ")
            
            for i in range(len(line_words)):
                
                if line_words[i] in self.word_mappings:
                    self.word_mappings[line_words[i]] += 1
                else:
                    self.word_mappings[line_words[i]] = 1
                
                if (i + 1) < len(line_words):
                    if f"{line_words[i]} {line_words[i+1]}" in self.bigram:
                        self.bigram[f"{line_words[i]} {line_words[i+1]}"] += 1
                    else:
                        self.bigram[f"{line_words[i]} {line_words[i+1]}"] = 1

    def predict(self, sentence):
        sentence = sentence.split(" ")
        bigram_count, word_count = self.bigram[f"{sentence[-2]} {sentence[-1]}"], self.word_mappings[f"{sentence[-2]}"]

        if bigram_count != None and word_count != None:
            probability = bigram_count / word_count
            return probability
        
    

if __name__ == '__main__':
    n_grams = N_GRAMS()
    intelligence = n_grams.predict("is intelligence")
    the = n_grams.predict("is the")
    our = n_grams.predict("is our") 
    to = n_grams.predict("is to")

    print(f"Intelligence Probability {intelligence}")
    print(f"The Probability {the}")
    print(f"Our Probability {our}")
    print(f"To Probability {to}")


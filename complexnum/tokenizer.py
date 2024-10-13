import re


class ConvertToToken:

    def __init__(self, keywords, string, tokens, SYMBOL):
        self.keywords = keywords
        self.string = string
        self.tokens = tokens
        self.symbol = SYMBOL

    def tokenize(self):
        tokenized_output = []
        tokenized_dict = []
        tokenized_output_w_spaces = []

        temp = re.split(
            rf"\b({'|'.join(map(re.escape, self.keywords))})\b|([^\w\s])", self.string
        )

        filtered_list = [x for x in temp if x and x.strip()]

        # Append each non-empty item to the tokenized_output_w_spaces
        tokenized_output_w_spaces.extend(filtered_list)
        # Remove trailing, leading whitespaces, and empty strings
        detail = [ele for ele in temp if ele and ele.strip()]

        # Tokenize the split list
        for ele in detail:
            if ele in self.keywords:
                tokenized_output.append(self.tokens[self.keywords.index(ele)])
            elif ele in self.symbol:
                tokenized_output.append(ele)
            else:
                tokenized_output.append(ele.strip())

        for ele in detail:
            tokenized_dict.append(
                {
                    "value": ele,
                    "type": (
                        "SYMBOL"
                        if ele in self.symbol
                        else "KEYWORD" if ele in self.keywords else "IDENTIFIER"
                    ),
                }
            )

        # Iterate over a copy of the list to avoid modifying it while iterating
        for item in tokenized_dict[:]:
            if not item["value"]:
                tokenized_dict.remove(item)
            elif "\n" in item["value"]:
                item["value"] = item["value"].replace("\n", "")

        return tokenized_output, tokenized_dict, tokenized_output_w_spaces

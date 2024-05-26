from nltk.corpus import wordnet

def get_word_synsets(word):
    synsets = wordnet.synsets(word)
    return synsets

def get_word_category(word):
    synsets = get_word_synsets(word)
    categories = []
    for synset in synsets:
        categories.extend(synset.topic_domains())
    return list(set(categories))

def categorize_words(words):
    categories = {}
    for word in words:
        word_categories = get_word_category(word)
        for category in word_categories:
            if category in categories:
                categories[category].append(word)
            else:
                categories[category] = [word]
    return categories

# words = {'unrelated', 'marked', 'comparing', 'reasoning', 'articles', 'result', 'misses', 'message', 'demonstration', 'situation', 'indication', 'harmful', 'monotonous' 'proved', 'opinion', 'range', 'concise', 'secondary', 'compare', 'complete', 'calculate', 'messy', 'justified', 'saving', 'harm', 'feel', 'helpful', 'carefully', 'established', 'digging', 'sufficient', 'height', 'actual', 'arranging', 'considerations', 'partly', 'analyze', 'enumeration', 'reflect', 'answered', 'meaning', 'illustrate', 'compared', 'accurate', 'evidence', 'deep', 'clarified',  'persuasion', 'description', 'prove', 'unsafe', 'angle', 'separately', 'fewer', 'accepted', 'locked', 'reading', 'valuable', 'characters', 'sloppy', 'explains', 'fine', 'organization', 'solved', 'perfect', 'core', 'dangers', 'glance', 'chain', 'key', 'flawed', 'warning', 'characteristics', 'normal', 'describes', 'plan', 'comprehensive', 'specific', 'features', 'speicific', 'easier', 'improve', 'logical', 'questions', 'error', 'argument', 'tedious', 'mind', 'solving', 'pleasing', 'common', 'discipline', 'subject', 'contrast', 'analogical', 'examples', 'learning', 'lazy', 'analytical', 'simpler', 'short', 'insight', 'shape', 'confused', 'direct', 'triangle', 'person', 'instructions', 'deeply', 'real', 'prepare', 'previous', 'separate', 'reason', 'reflected', 'based', 'topic', 'providing', 'accurately', 'idea', 'satisfied', 'broadens', 'illustrated', 'conclusion', 'difficult', 'citing', 'attention', 'habits', 'significance', 'details', 'calculation', 'obtuse', 'deepen', 'claim', 'introduction', 'substantiated', 'solves', 'harmfulness', 'onesided', 'liking', 'generalized', 'simplify', 'represents', 'priorities', 'foundation', 'benefit', 'explained', 'fast', 'disasters', 'protect', 'units', 'worth', 'analysis', 'breaking', 'innovative', 'explanations', 'choice', 'type', 'serve', 'rational', 'nice', 'marks', 'read', 'instruction', 'compact', 'suggestions', 'sequence', 'orderliness', 'varied', 'extra', 'summarized', 'understand', 'analyzing', 'impossible', 'scientific', 'content', 'correct', 'organized', 'symmetrical', 'crude',  'reasons', 'step', 'memorable', 'sense', 'specifics', 'informative', 'logic', 'prominent', 'natural', 'response', 'solutions', 'directly', 'characteristic', 'contrary', 'text', 'quality', 'methods', 'descriptive', 'reliable', 'verbose', 'representational', 'impeccable', 'excellent', 'indepth', 'flaws', 'afraid', 'introduced', 'primary', 'mathematical', 'ideas', 'wellfounded', 'question', 'provide', 'omits', 'emphasized', 'functions', 'language', 'volume', 'analogy', 'profound', 'ability', 'feedback', 'character', 'set', 'clarity', 'skills', 'reasonable', 'properly', 'prevention', 'blunt', 'useless', 'unconvincing', 'truth', 'cognition', 'misleading', 'weak', 'easily', 'representative', 'protective', 'strong', 'cognitively', 'suggestion', 'ai', 'convoluted', 'merit', 'carried', 'effectively', 'stick', 'poor', 'complicated', 'thoughtful', 'enlightening', 'missing', 'sentences', 'shine', 'comfortable', 'avoid', 'write', 'persuasive', 'measures', 'monotonic', 'unfounded', 'lack', 'professional', 'complex', 'traditional', 'main', 'procedure', 'horizon', 'barely', 'simply', 'dig', 'concrete', 'achieve', 'listing', 'compelling', 'deal', 'develop', 'partially', 'behavior', 'precise', 'credibility', 'perfectly', 'correlation', 'verify', 'comparison', 'rigid', 'applies', 'statement', 'length', 'moving', 'support', 'role', 'consistent', 'hazards', 'fail', 'pay', 'detailed', 'sound', 'multiple', 'time', 'form', 'solution', 'methodical', 'derivation', 'depth', 'verification', 'advice', 'grasp', 'explain', 'apply', 'authenticity', 'misunderstood', 'refreshing', 'explanation', 'proof', 'flawlessly', 'people', 'simple', 'risks', 'simplistic', 'sections', 'careful', 'insightful', 'structure', 'highlight', 'expressed', 'shapes', 'purpose', 'rigorous', 'unique', 'listed', 'taste', 'caused', 'answering', 'straightforward', 'causal', 'single', 'acceptable', 'simplified', 'inadequate', 'teaches', 'beautiful', 'bring', 'responses', 'easy', 'identify', 'introduces', 'demonstrated', 'tight', 'effective', 'wrong', 'understanding', 'meaningful', 'downside', 'degree', 'waste', 'concept', 'quick', 'rich', 'title', 'feeling', 'smooth', 'view', 'aspects', 'timeconsuming', 'hit', 'situations', 'true', 'solve', 'closely', 'applied', 'relationship', 'broad', 'welldocumented', 'surprising', 'suggested', 'proceed', 'finally', 'answer', 'convincing', 'thinking', 'conviction', 'shallow', 'popular', 'passage', 'original', 'confusing', 'dealt', 'method', 'highend', 'suggests', 'expression', 'definition', 'summary', 'inference', 'detail', 'pile', 'calculated', 'final', 'user', 'knowledge', 'process', 'acute', 'norm', 'application', 'preventive', 'advantages', 'power', 'steps', 'practical', 'moment', 'convenient', 'focus', 'formulas', 'integrity', 'hard', 'opinions', 'atmosphere', 'segments', 'gap', 'illustrates', 'answers', 'allowing', 'subtitles', 'clearer', 'bad', 'analyzed', 'stytle', 'distinguish', 'connotation', 'extraordinary', 'lacks', 'aware', 'algorithm', 'applicable', 'defects', 'column', 'formula', 'accept', 'visible', 'believable', 'simplest', 'clearest', 'knowledgeable'}
words = set()
with open('keywords.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words.add(line.strip())

word_categories = categorize_words(words)
f = open("word_categories.txt", "w")
for category, words in word_categories.items():
    print(category, words)
    print(category, words, file=f)


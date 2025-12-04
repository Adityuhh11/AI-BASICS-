
from copy import deepcopy
from logic.biconditional import Biconditional
from logic.implication import Implication
from logic.negation import Not


def is_in(knowledge, query):
    for conjunct in knowledge.conjuncts:
        if conjunct.is_same(query):
            return True
    return False

def check_proven(knowledge, query):
    """
        checks whether the query is currently proven or disproven in the knowledge base.

        returns:
        - True: if the query is contained
        - False: if the negation of the query is contained.
        - None: else
    """
    if is_in(knowledge,query):
        return True
    elif is_in(knowledge,Not(query)):
        return False
    else:
       return None

def get_inferrable_knowledge(knowledge):
    """
        Takes a knowledge base and finds all sentences that can be inferred.

        returns a list of sentences that can be inferred from the knowlede base.
    """
    inferrable_knowledge = []
    for sentence in knowledge.conjuncts:
        if type(sentence) is Implication:
            if is_in(knowledge,sentence.antecedent) and not is_in(knowledge,sentence.consequent):
                inferrable_knowledge.append(sentence.consequent)
        if type(sentence) is Biconditional:
            left_known = is_in(knowledge,sentence.left)
            right_known = is_in(knowledge, sentence.right)

            if left_known and not right_known:
                inferrable_knowledge.append(sentence.right)
            elif right_known and not left_known:
                inferrable_knowledge.append(sentence.left)
    return inferrable_knowledge

            


def forward_search(knowledge, query):
    """
        solved the query by doing forward search.
    
        parameters:
        - The knowledge base containing all knowledge. This is an And formula.
        - The query to check. This is expected to be a symbol.

        returns:
        - True: if the query can be proven
        - False: if the query can be disproven
        - None: if the query can't be proven or disproven
    """

    # copying the knowledge base so we don't accidentally modify an input parameter.
    knowledge_base = deepcopy(knowledge)

    while True:
        # 1. Check if the query is already solved with current knowledge
        result = check_proven(knowledge_base, query)
        if result is not None:
            return result

        # 2. Find new knowledge that can be inferred from the current base
        inferred_sentences = get_inferrable_knowledge(knowledge_base)

        # 3. If no new knowledge can be inferred, we are stuck.
        if not inferred_sentences:
            return None

        # 4. Add the newly inferred sentences to our knowledge base and repeat
        for sentence in inferred_sentences:
            knowledge_base.add(sentence)

    

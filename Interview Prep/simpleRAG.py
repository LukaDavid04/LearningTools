import numpy as np

class VectorStore:
    def __init__(self) -> None:
        self.vector_dict = {}

    def add(self, doc_id: str, embedding: list[float], text: str) -> None:
        if doc_id not in self.vector_dict:
            self.vector_dict[doc_id] = (np.array(embedding), text)
        else:
            raise ValueError(f"The ID '{doc_id}' is already used in the Vector Store.")

    @staticmethod
    def cosine_similarity(query_vec, doc_vec):
        dot_prod = np.dot(query_vec, doc_vec)
        norm_query = np.linalg.norm(query_vec)
        norm_doc = np.linalg.norm(doc_vec)
        if norm_query == 0 or norm_doc == 0:   # guard against zero vectors
            return 0.0
        return dot_prod / (norm_query * norm_doc)

    def search(self, query_embedding: list[float], k: int) -> list[tuple[str, float]]:
        if not self.vector_dict:
            return []
        query_vector = np.array(query_embedding)
        topk = []  # running list of (doc_id, score) — at most k entries
        for doc_id, (embedding, text) in self.vector_dict.items():
            curr = self.cosine_similarity(query_vector, embedding)
            if len(topk) < k:
                topk.append((doc_id, curr))
            else:
                # index of the weakest score currently held
                min_idx = min(range(len(topk)), key=lambda i: topk[i][1])
                if curr > topk[min_idx][1]:
                    topk[min_idx] = (doc_id, curr)
        topk.sort(key=lambda x: x[1], reverse=True)   # highest similarity first
        return topk
            
    def pprint(self):
        print(self.vector_dict)

store = VectorStore()
store.add("d1", [1.0, 0.0], "billing question")
store.add("d2", [0.0, 1.0], "password reset")
store.add("d3", [0.9, 0.1], "invoice issue")

store.pprint()

print(store.search([1.0, 0.0], k=2))

# # -> [("d1", 1.0), ("d3", ~0.994)]
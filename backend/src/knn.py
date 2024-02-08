from annoy import AnnoyIndex
import json
import pandas as pd
import numpy as np


class KNN:
    def __init__(self):
        self.dimension = 1024
        self.n_trees = 10
        self.distance = 'angular'

        print('Loading data...')
        self.df = pd.read_csv('../data/good_data.csv')


        print('Loading index...')
        self.weighted_index = AnnoyIndex(self.dimension, self.distance)
        self.weighted_index.load('weighted_item_embeddings.ann')

        self.unweighted_index = AnnoyIndex(self.dimension, self.distance)
        self.unweighted_index.load('unweighted_item_embeddings.ann')
    
    def find_nearest_neighbors(self, embedding, weighted=True, n_neighbors=5):
        index = self.weighted_index if weighted else self.unweighted_index

        def get_distance(embedding1, embedding2):
            return np.dot(embedding1, embedding2)

        def format_rows(rows, distances):
            output = []
            for i, (_, row) in enumerate(rows.iterrows()):
                weighted_terms_object = [json.loads(t) for t in json.loads(row['weighted_terms'])]
                weighted_terms = [(t['term'], t['weight']) for t in weighted_terms_object]

                weighted_distance = get_distance(embedding, json.loads(row['embeddings_weighted']))
                unweighted_distance = get_distance(embedding, json.loads(row['embeddings_unweighted']))

                output.append({
                    'i': i + 1,
                    'name': row['name'],
                    'brand': row['brand'] if not pd.isna(row['brand']) else '-',
                    'image_url': row['image_url'] if not pd.isna(row['image_url']) else '',
                    'weighted_terms': weighted_terms,
                    'unweighted_terms': row['unweighted_terms'],
                    'weighted_distance': weighted_distance,
                    'unweighted_distance': unweighted_distance,
                })

            return output

        nearest_ids = index.get_nns_by_vector(embedding, n_neighbors, include_distances=True)
        nearest_neighbors = self.df.iloc[nearest_ids[0]]

        return format_rows(nearest_neighbors, nearest_ids[1])
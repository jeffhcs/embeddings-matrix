import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from embed import embed


def get_similarity(e1, e2, metric):
    
    assert metric in ['cosine', 'dot', 'l2'], 'Invalid metric'

    e1 = np.array(e1) if not isinstance(e1, np.ndarray) else e1
    e2 = np.array(e2) if not isinstance(e2, np.ndarray) else e2

    dot_product = np.dot(e1, e2)

    if metric == 'dot':
        return dot_product
    elif metric == 'cosine':
        norm_e1 = np.linalg.norm(e1)
        norm_e2 = np.linalg.norm(e2)
        cosine_similarity = dot_product / (norm_e1 * norm_e2)
        return cosine_similarity
    elif metric == 'l2':
        l2_distance = np.linalg.norm(e1 - e2)
        return l2_distance

def compare(labels, embeddings, metric):
    df = pd.DataFrame(columns=labels, index=labels)

    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            similarity = get_similarity(embeddings[i], embeddings[j], metric)
            df.iloc[i,j] = similarity
            df.iloc[j,i] = similarity

    np.fill_diagonal(df.values, 0 if metric == 'l2' else 1)

    df = df.astype(float)

    return df

def plot(df):
    plt.figure(figsize=(10,8))
    sns.heatmap(df, annot=True, cmap="YlGnBu")
    plt.show()

def get_plot(texts, metric, model):
    embeddings = embed(texts, model)  # embed and compare functions need to be defined
    df = compare(texts, embeddings, metric)
    
    # Set monospace font globally
    plt.rc('font', family='monospace')
    
    plt.figure(figsize=(10,8))
    # Use fmt='.3f' to format annotations with 3 digits
    sns.heatmap(df, annot=True, fmt='.3f', cmap="YlGnBu")
    
    plt.title(f'Model: {model}, Metric: {metric}', fontsize=12)
    
    output = BytesIO()
    plt.savefig(output, format='png', bbox_inches='tight')
    output.seek(0)

    plt.close()
    
    return output
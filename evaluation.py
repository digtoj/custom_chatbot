from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from datasets import Dataset

from const import prototypA, prototypB
from dataset_evaluation import questions, ground_truth
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)
from dotenv import load_dotenv
import plotly.graph_objects as go

load_dotenv()
# Define LLM
llm = ChatOpenAI( temperature=0)


def evaluate_by_vectore(prototyp , vector_store):
    
    retriever = vector_store.as_retriever()

    # Define prompt template
    template = """You are an assistant for question-answering tasks.
    you can speak german. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use two sentences maximum and keep the answer concise.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    retriever_chain =  (
        {"context": retriever,  "question": RunnablePassthrough()} 
        | prompt 
        | llm
        | StrOutputParser()
    )

    answers = []
    contexts = []
            # Inference
    for query in questions:
        answers.append(retriever_chain.invoke(query))
        contexts.append([docs.page_content for docs in retriever.get_relevant_documents(query)])

        # To dict
        data = {
            "question": questions,
            "answer": answers,
            "contexts": contexts,
            "ground_truth": ground_truth
        } 
    # Convert dict to dataset
    dataset = Dataset.from_dict(data)
    result = evaluate(
    dataset = dataset, 
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy,
    ],
)
    print(result)

    data = {
    'context_precision': result['context_precision'],
    'faithfulness': result['faithfulness'],
    'answer_relevancy': result['answer_relevancy'],
    'context_recall': result['context_recall']
}
    
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(data.values()),
        theta=list(data.keys()),
        fill='toself',
        name='Ensemble RAG'
    ))

    title ='RAG - Evaluation für das '+prototyp

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True,
        
        title=title,
        width=800,
    )

    fig.show() 



    

    
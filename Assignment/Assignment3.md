# Assignment 3:Deep Learning Assignment: English-to-French Machine Translation

## Deadline
2024-11-22 11:59 PM, no late submissions will be accepted.

## Objective
In this assignment, you will build a sequence-to-sequence model using the Transformer architecture to translate English sentences into French. You will:

1. Use the provided English-to-French dataset.
2. Implement the Transformer model as the backbone for both the encoder and decoder.
3. Train the model from scratch without using any pre-trained embeddings.
4. Utilize **PyTorch Lightning** for model implementation and **Weights & Biases (W&B)** for experiment tracking.

## Instructions

### Part 1: Data Preparation (20%)
- Use the provided dataset (I posted it on Edstem) for English-to-French translation.
- Preprocess the data:
  - Tokenize the text using a subword tokenization method (e.g., Byte-Pair Encoding).
  - Create vocabulary dictionaries for both English and French.
  - Split the dataset into training, validation, and test sets.

### Part 2: Model Implementation (30%)
- Implement a sequence-to-sequence model using the Transformer architecture:
  - **Encoder**: Use multi-head self-attention and positional encoding.
  - **Decoder**: Use masked multi-head self-attention, encoder-decoder attention, and positional encoding.
  - **Output Layer**: Use a linear layer followed by a softmax activation.
- Do **not** use any pre-trained embeddings or models for this task. Implement the embedding layers from scratch.

### Part 3: Training with PyTorch Lightning (30%)
- Use **PyTorch Lightning** to structure your code and simplify the training process.
- Set up an appropriate training loop with the following considerations:
  - Implement early stopping based on validation loss.
  - Use a suitable optimizer (e.g., AdamW) and a learning rate scheduler.
  - Apply techniques such as gradient clipping and mixed precision training for improved performance.

### Part 4: Experiment Tracking with Weights & Biases (W&B)
- Use **Weights & Biases (W&B)** to log the following metrics:
  - Training and validation loss over epochs.
  - BLEU score on the validation set.
- At the end of the assignment, provide the **W&B link** to your experiment dashboard.

### Part 5: Evaluation and Report (20%)
- Evaluate your model on the test set using the BLEU score as the main evaluation metric.
- Perform a qualitative analysis by showcasing a few examples of translated sentences.
- Write a brief report (1-2 pages, PDF format) that includes:
  - A summary of the dataset and preprocessing steps.
  - An overview of the model architecture.
  - Training strategies and experimental setup (e.g., optimizer, learning rate scheduler).
  - Evaluation results (including BLEU score) and analysis of sample translations.
  - Challenges faced during the implementation and how you overcame them.

## Optional Extensions (2 Bonus Points)
- Implement beam search or another decoding strategy for better translation quality.
- Experiment with different tokenization methods (e.g., SentencePiece).


## Deliverables
1. Code files (train.py. inference.py and all related files) with a README for instructions on running the code.
2. A PDF report (1-2 pages) summarizing the experiment.
3. A link to your Weights & Biases experiment dashboard with logged metrics.

## Submission
Submit your code, report, and W&B link by the specified deadline through the gradescore.

For each team, only one submission is required.
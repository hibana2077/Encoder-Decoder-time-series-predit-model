<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2024-05-16 22:56:10
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2024-05-17 11:30:26
 * @FilePath: \Encoder-Decoder-time-series-predit-model\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Stock Price Movement Prediction Model Based on LSTM Autoencoder

<p align="center">
    <img src="https://skillicons.dev/icons?i=pytorch,py,docker" /><br>
</p>

## Introduction

## Abstract

In this study, we propose a novel approach for predicting stock price movements using an LSTM-based Autoencoder model. Initially, we train an autoencoder where both the input and output are the relative price changes over a given time interval, denoted as \(\Delta T\). The LSTM autoencoder is designed to capture the temporal dependencies in stock price fluctuations. Upon successful training, the autoencoder parameters are frozen to preserve the learned temporal representations. Subsequently, we augment this model by adding five fully connected (dense) layers to function as a classifier, which is then trained to enhance predictive accuracy.

The LSTM autoencoder consists of an encoder \(E(x_t)\) and a decoder \(D(y_t)\), where \(x_t\) and \(y_t\) represent the relative price changes over \(\Delta T\) at time \(t\). The objective is to minimize the reconstruction loss \(L_{rec} = \| x_t - D(E(x_t)) \|^2\), ensuring the encoder learns a compact representation \(z_t = E(x_t)\). The encoder is composed of LSTM units, formulated as:
\[ h_t = \text{LSTM}(x_t, h_{t-1}, c_{t-1}) \]
where \(h_t\) denotes the hidden state and \(c_t\) the cell state at time \(t\).

In the classifier stage, the frozen autoencoder outputs \(z_t\) are fed into the dense layers, trained with a cross-entropy loss \(L_{cls} = -\sum y_i \log \hat{y}_i\), where \(y_i\) and \(\hat{y}_i\) represent the true and predicted class labels respectively. This two-stage training approach leverages the robust feature extraction capabilities of the LSTM autoencoder and refines the predictions through additional classification layers.

Our experimental results demonstrate that this model significantly improves the accuracy of stock price movement predictions, validating the effectiveness of incorporating LSTM autoencoders in financial time series analysis.

## Results

## Run
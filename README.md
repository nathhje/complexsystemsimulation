# Using circadian activity rhythm as an early warning sign for manic and depressed episodes in people with bipolar disorder.
We recreated a model first proposed by Hadaeghi et al. (2016) to simulate the circadian activity rhythm, mainly in people with bipolar disorder who are experiencing a manic or depressed episode. The eventual goal of this area of research is to detect these episodes before they happen so people with the disorder can prepare for them. This was a first step in the process. 

The model should be run from the main.py file in this directory. It uses the model.py file in the classes directory to run the model and the model.py functions uses the function in functions_guy.py in the helpers directory. In the helpers directory there are two files named changingAbifurcation.py and changingBbifurcation.py that create bifurcation maps for the neuronal activity x as a function of A and B respectively. Figures with examples of output of the bifurcation map, time series of neuronal activity x as a function of iterations n and the output as a function of days can be found in the doc directory, together with the powerpoint presentation that we presented about the project.

## References

Hadaeghi, F., Hashemi Golpayegani, M. R., Jafari, S., & Murray, G. (2016). Toward a complex system understanding of bipolar disorder: A chaotic model of abnormal circadian activity rhythms in euthymic bipolar disorder. Australian & New Zealand Journal of Psychiatry, 50(8), 783-792.

Rulkov, N. F. (2007). A map-based model of the cardiac action potential. arXiv preprint arXiv:0708.1173.


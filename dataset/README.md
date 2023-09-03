# Cross-domain scientific paper aspect dataset

This part contains 200 abstracts to Russian-language scientific papers of 10 domains: Biology and Medicine, Computer science, History and Philology, Journalism, Law, Linguistics, Mathematics, Pedagogy, Physics, Psychology.
Each directory contains 20 texts of the corresponding domain annotated with 4 aspects: Task, Contribution (Contrib), Method, and Conclusion (Conc).
Each token in the texts is labeled with one or two aspects to which it is assigned or with the 'O' tag if it does not belong to any aspect.

The dataset contains 836 aspect mentions, which cover 10,287 tokens. 

This table shows the distribution of aspect types over different domains in our dataset:

| Domain              |Task|Contribution|Method|Conclusion|
|---------------------|----|------------|------|----------|
| Biology & Medicine  |   6|          30|    18|        52|      
| Computer Science    |  17|          46|    10|         4|
| History & Philology |   4|          43|     5|        50|
| Journalism          |  10|          29|     0|         5|
| Law                 |  26|          50|     2|        38|
| Linguistics         |  15|          38|     9|        10|
| Math                |  11|          46|    13|         6|
| Pedagogy            |  29|          50|     1|         4|
| Physics             |   7|          48|    14|        18|
| Psychology          |  15|          34|     9|        14|

For this experiment, we train models using the steps laid out here: https://stanfordnlp.github.io/stanza/training.html. 
Set the UDBASE environment variable to the desired training folder (i.e. Universal-Dependencies-2.8.1/faroese-leaky/Unlabeled) and then run the following commands to train and evaluate the models.
These can be run in parallel for faster computation.

For training:

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Faroese-FarPaHC --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Faroese-FarPaHC --wordvec_pretrain_file /home/nkrasner/stanza_resources/fo/pretrain/farpahc.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_German-HDT --gold \
\>\> python stanza/utils/training/run_depparse.py UD_German-HDT --wordvec_pretrain_file /home/nkrasner/stanza_resources/de/pretrain/gsd.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Afrikaans-AfriBooms --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Afrikaans-AfriBooms --wordvec_pretrain_file /home/nkrasner/stanza_resources/af/pretrain/afribooms.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Danish-DDT --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Danish-DDT --wordvec_pretrain_file /home/nkrasner/stanza_resources/da/pretrain/ddt.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Icelandic-IcePaHC --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Icelandic-IcePaHC --wordvec_pretrain_file /home/nkrasner/stanza_resources/is/pretrain/icepahc.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Norwegian-Bokmaal --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Norwegian-Bokmaal --wordvec_pretrain_file /home/nkrasner/stanza_resources/nb/pretrain/bokmaal.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Swedish-LinES --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Swedish-LinES --wordvec_pretrain_file /home/nkrasner/stanza_resources/sv/pretrain/talbanken.pt


For evaluation:

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Faroese-FarPaHC --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Faroese-FarPaHC --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/fo/pretrain/farpahc.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_German-HDT --gold \
\>\> python stanza/utils/training/run_depparse.py UD_German-HDT --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/de/pretrain/gsd.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Afrikaans-AfriBooms --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Afrikaans-AfriBooms --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/af/pretrain/afribooms.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Danish-DDT --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Danish-DDT --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/da/pretrain/ddt.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Icelandic-IcePaHC --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Icelandic-IcePaHC --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/is/pretrain/icepahc.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Norwegian-Bokmaal --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Norwegian-Bokmaal --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/nb/pretrain/bokmaal.pt

\>\> python stanza/utils/datasets/prepare_depparse_treebank.py UD_Swedish-LinES --gold \
\>\> python stanza/utils/training/run_depparse.py UD_Swedish-LinES --score_test --save_dir saved_models/depparse/diverse --wordvec_pretrain_file /home/nkrasner/stanza_resources/sv/pretrain/talbanken.pt

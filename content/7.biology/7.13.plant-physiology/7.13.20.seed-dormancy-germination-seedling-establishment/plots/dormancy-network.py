# Integration of environmental signals in seed dormancy and germination through the ABA:GA balance (SBGN
# Activity Flow, simplified; after Finch-Savage & Leubner-Metzger 2006 and Taiz et al. 6e, Fig. 18.5).
# Red light (phyB, Pfr) degrades PIF1/PIL5, which otherwise represses GA3ox and induces GA2ox and ABA
# synthesis; cold stratification raises GA3ox and lowers ABA; nitrate (via NLP8) induces CYP707A2, the
# ABA 8'-hydroxylase; karrikins from smoke act through KAI2-MAX2 and the degradation of SMAX1; DOG1 deepens
# dormancy by enhancing ABA signalling (inhibiting the PP2C AHG1); after-ripening lowers DOG1 activity and ABA
# sensitivity. ABA, via ABI3/ABI5, keeps the seed dormant; GA, by degrading DELLA (RGL2), promotes
# endosperm weakening and embryo growth.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(21, 10)
d = network.Diagram(ax)
d.compartment("seed", (3.3, 0.4, 20.7, 9.6), "Seed", token="cytoplasm", label_pos="tr")
d.perturbation("red", (1.6, 8.6), "Red light", token="negative")
d.perturbation("cold", (1.6, 6.6), "Cold, moist", token="channel")
d.perturbation("no3", (1.6, 4.6), "Nitrate", token="neutral")
d.perturbation("kar", (1.6, 2.6), "Smoke (karrikin)", token="highlight")
d.perturbation("ar", (1.6, 0.9), "Dry storage", token="neutral")
d.activity("phy", (5.4, 8.6), "phyB (Pfr)", token="receptor")
d.activity("pif", (8.6, 8.6), "PIF1 / PIL5", token="protein")
d.activity("ga3", (12.2, 8.0), "GA3ox", token="enzyme")
d.activity("ga2", (12.2, 6.6), "GA2ox", token="enzyme")
d.activity("nced", (8.6, 5.0), "NCED (ABA synthesis)", token="enzyme")
d.activity("cyp", (8.6, 3.6), "CYP707A2", token="enzyme")
d.activity("kai", (5.4, 2.6), "KAI2–MAX2", token="receptor")
d.activity("smax", (8.6, 2.2), "SMAX1", token="protein")
d.activity("dog1", (8.6, 0.95), "DOG1", token="protein")
d.activity("ga", (15.4, 7.3), "GA", token="metabolite")
d.activity("aba", (12.2, 4.3), "ABA", token="drug")
d.activity("della", (15.4, 5.6), "DELLA (RGL2)", token="negative")
d.activity("abi", (15.4, 3.0), "ABI3 / ABI5", token="protein")
d.phenotype("germ", (19.0, 5.6), "Germination")
d.phenotype("dorm", (19.0, 2.0), "Dormancy")
d.connect("red", "phy", "positive")
d.connect("phy", "pif", "negative")
d.connect("pif", "ga3", "negative", via=[(10.4, 8.6), (10.4, 8.0)])
d.connect("pif", "ga2", "positive", via=[(10.4, 8.6), (10.4, 6.6)])
d.connect("pif", "nced", "positive")
d.connect("cold", "ga3", "positive", via=[(3.1, 7.4), (11.0, 7.4)])
d.connect("no3", "cyp", "positive", via=[(3.1, 4.6), (3.1, 3.6)])
d.connect("kar", "kai", "positive")
d.connect("kai", "smax", "negative")
d.connect("smax", "ga3", "negative", via=[(10.7, 2.2), (10.7, 7.75)], dashed=True)
d.connect("ar", "dog1", "negative")
d.connect("ga3", "ga", "positive")
d.connect("ga2", "ga", "negative")
d.connect("nced", "aba", "positive")
d.connect("cyp", "aba", "negative")
d.connect("ga", "della", "negative")
d.connect("aba", "abi", "positive")
d.connect("dog1", "abi", "positive", via=[(13.8, 0.95)])
d.connect("della", "germ", "negative")
d.connect("abi", "dorm", "positive")
d.connect("abi", "germ", "negative", via=[(17.3, 3.0)])
d.connect("della", "abi", "positive", dashed=True)
d.connect("aba", "ga", "negative", via=[(13.6, 4.9)], dashed=True)

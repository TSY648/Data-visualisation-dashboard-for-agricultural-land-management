This project is a web-based dashboard designed to visualise agricultural data across Indian states and crops. It is developed using Django and Bootstrap, with data analysis performed in Python (Jupyter Notebook).

Directory Content:
------------------
1. Dashboard structure:
dashboard
├─ app01
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     └─ __init__.cpython-39.pyc
│  ├─ models.py
│  ├─ static
│  │  ├─ css
│  │  ├─ img
│  │  │  ├─ Arecanut_Area_Production.png
│  │  │  ├─ Arecanut_Area_Yield.png
│  │  │  ├─ Arecanut_bubble.png
│  │  │  ├─ Arecanut_Production_Yield.png
│  │  │  ├─ Arhar_Area_Production.png
│  │  │  ├─ Arhar_Area_Yield.png
│  │  │  ├─ Arhar_bubble.png
│  │  │  ├─ Arhar_Production_Yield.png
│  │  │  ├─ Bajra_Area_Production.png
│  │  │  ├─ Bajra_Area_Yield.png
│  │  │  ├─ Bajra_bubble.png
│  │  │  ├─ Bajra_Production_Yield.png
│  │  │  ├─ Banana_Area_Production.png
│  │  │  ├─ Banana_Area_Yield.png
│  │  │  ├─ Banana_bubble.png
│  │  │  ├─ Banana_Production_Yield.png
│  │  │  ├─ Barley_Area_Production.png
│  │  │  ├─ Barley_Area_Yield.png
│  │  │  ├─ Barley_bubble.png
│  │  │  ├─ Barley_Production_Yield.png
│  │  │  ├─ Black pepper_Area_Production.png
│  │  │  ├─ Black pepper_Area_Yield.png
│  │  │  ├─ Black pepper_bubble.png
│  │  │  ├─ Black pepper_Production_Yield.png
│  │  │  ├─ Cardamom_Area_Production.png
│  │  │  ├─ Cardamom_Area_Yield.png
│  │  │  ├─ Cardamom_bubble.png
│  │  │  ├─ Cardamom_Production_Yield.png
│  │  │  ├─ Castor seed_Area_Production.png
│  │  │  ├─ Castor seed_Area_Yield.png
│  │  │  ├─ Castor seed_bubble.png
│  │  │  ├─ Castor seed_Production_Yield.png
│  │  │  ├─ Cereals_Area_Production.png
│  │  │  ├─ Cereals_Area_Yield.png
│  │  │  ├─ Cereals_bubble.png
│  │  │  ├─ Cereals_Production_Yield.png
│  │  │  ├─ Coarse Cereals_Area_Production.png
│  │  │  ├─ Coarse Cereals_Area_Yield.png
│  │  │  ├─ Coarse Cereals_bubble.png
│  │  │  ├─ Coarse Cereals_Production_Yield.png
│  │  │  ├─ Coconut_Area_Production.png
│  │  │  ├─ Coconut_Area_Yield.png
│  │  │  ├─ Coconut_bubble.png
│  │  │  ├─ Coconut_Production_Yield.png
│  │  │  ├─ Coffee_Area_Production.png
│  │  │  ├─ Coffee_Area_Yield.png
│  │  │  ├─ Coffee_bubble.png
│  │  │  ├─ Coffee_Production_Yield.png
│  │  │  ├─ Coriander_Area_Production.png
│  │  │  ├─ Coriander_Area_Yield.png
│  │  │  ├─ Coriander_bubble.png
│  │  │  ├─ Coriander_Production_Yield.png
│  │  │  ├─ Cost Comparison ARHAR.png
│  │  │  ├─ Cost Comparison COTTON.png
│  │  │  ├─ Cost Comparison GRAM.png
│  │  │  ├─ Cost Comparison GROUNDNUT.png
│  │  │  ├─ Cost Comparison MAIZE.png
│  │  │  ├─ Cost Comparison MOONG.png
│  │  │  ├─ Cost Comparison PADDY.png
│  │  │  ├─ Cost Comparison RAPESEED AND MUSTARD.png
│  │  │  ├─ Cost Comparison SUGARCANE.png
│  │  │  ├─ Cost Comparison WHEAT.png
│  │  │  ├─ Cost of Cultivation for Crop ARHAR.png
│  │  │  ├─ Cost of Cultivation for Crop COTTON.png
│  │  │  ├─ Cost of Cultivation for Crop GRAM.png
│  │  │  ├─ Cost of Cultivation for Crop GROUNDNUT.png
│  │  │  ├─ Cost of Cultivation for Crop MAIZE.png
│  │  │  ├─ Cost of Cultivation for Crop MOONG.png
│  │  │  ├─ Cost of Cultivation for Crop PADDY.png
│  │  │  ├─ Cost of Cultivation for Crop RAPESEED AND MUSTARD.png
│  │  │  ├─ Cost of Cultivation for Crop SUGARCANE.png
│  │  │  ├─ Cost of Cultivation for Crop WHEAT.png
│  │  │  ├─ Cost of Cultivation for State Andhra Pradesh.png
│  │  │  ├─ Cost of Cultivation for State Bihar.png
│  │  │  ├─ Cost of Cultivation for State Gujarat.png
│  │  │  ├─ Cost of Cultivation for State Haryana.png
│  │  │  ├─ Cost of Cultivation for State Karnataka.png
│  │  │  ├─ Cost of Cultivation for State Madhya Pradesh.png
│  │  │  ├─ Cost of Cultivation for State Maharashtra.png
│  │  │  ├─ Cost of Cultivation for State Orissa.png
│  │  │  ├─ Cost of Cultivation for State Punjab.png
│  │  │  ├─ Cost of Cultivation for State Rajasthan.png
│  │  │  ├─ Cost of Cultivation for State Tamil Nadu.png
│  │  │  ├─ Cost of Cultivation for State Uttar Pradesh.png
│  │  │  ├─ Cost of Cultivation for State West Bengal.png
│  │  │  ├─ Cost of Production for Crop ARHAR.png
│  │  │  ├─ Cost of Production for Crop COTTON.png
│  │  │  ├─ Cost of Production for Crop GRAM.png
│  │  │  ├─ Cost of Production for Crop GROUNDNUT.png
│  │  │  ├─ Cost of Production for Crop MAIZE.png
│  │  │  ├─ Cost of Production for Crop MOONG.png
│  │  │  ├─ Cost of Production for Crop PADDY.png
│  │  │  ├─ Cost of Production for Crop RAPESEED AND MUSTARD.png
│  │  │  ├─ Cost of Production for Crop SUGARCANE.png
│  │  │  ├─ Cost of Production for Crop WHEAT.png
│  │  │  ├─ Cost of Production for State Andhra Pradesh.png
│  │  │  ├─ Cost of Production for State Bihar.png
│  │  │  ├─ Cost of Production for State Gujarat.png
│  │  │  ├─ Cost of Production for State Haryana.png
│  │  │  ├─ Cost of Production for State Karnataka.png
│  │  │  ├─ Cost of Production for State Madhya Pradesh.png
│  │  │  ├─ Cost of Production for State Maharashtra.png
│  │  │  ├─ Cost of Production for State Orissa.png
│  │  │  ├─ Cost of Production for State Punjab.png
│  │  │  ├─ Cost of Production for State Rajasthan.png
│  │  │  ├─ Cost of Production for State Tamil Nadu.png
│  │  │  ├─ Cost of Production for State Uttar Pradesh.png
│  │  │  ├─ Cost of Production for State West Bengal.png
│  │  │  ├─ Cotton seed_Area_Production.png
│  │  │  ├─ Cotton seed_Area_Yield.png
│  │  │  ├─ Cotton seed_bubble.png
│  │  │  ├─ Cotton seed_Production_Yield.png
│  │  │  ├─ Cotton(lint)_Area_Production.png
│  │  │  ├─ Cotton(lint)_Area_Yield.png
│  │  │  ├─ Cotton(lint)_bubble.png
│  │  │  ├─ Cotton(lint)_Production_Yield.png
│  │  │  ├─ datafile(1)_head.png
│  │  │  ├─ datafile(1)_statistic.png
│  │  │  ├─ datafile(2)_head.png
│  │  │  ├─ datafile(2)_statistic.png
│  │  │  ├─ Dry chilies_Area_Production.png
│  │  │  ├─ Dry chilies_Area_Yield.png
│  │  │  ├─ Dry chilies_bubble.png
│  │  │  ├─ Dry chilies_Production_Yield.png
│  │  │  ├─ Dry ginger_Area_Production.png
│  │  │  ├─ Dry ginger_Area_Yield.png
│  │  │  ├─ Dry ginger_bubble.png
│  │  │  ├─ Dry ginger_Production_Yield.png
│  │  │  ├─ Garlic_Area_Production.png
│  │  │  ├─ Garlic_Area_Yield.png
│  │  │  ├─ Garlic_bubble.png
│  │  │  ├─ Garlic_Production_Yield.png
│  │  │  ├─ Gram_Area_Production.png
│  │  │  ├─ Gram_Area_Yield.png
│  │  │  ├─ Gram_bubble.png
│  │  │  ├─ Gram_Production_Yield.png
│  │  │  ├─ Groundnut_Area_Production.png
│  │  │  ├─ Groundnut_Area_Yield.png
│  │  │  ├─ Groundnut_bubble.png
│  │  │  ├─ Groundnut_Production_Yield.png
│  │  │  ├─ Jowar_Area_Production.png
│  │  │  ├─ Jowar_Area_Yield.png
│  │  │  ├─ Jowar_bubble.png
│  │  │  ├─ Jowar_Production_Yield.png
│  │  │  ├─ Jute & Mesta_Area_Production.png
│  │  │  ├─ Jute & Mesta_Area_Yield.png
│  │  │  ├─ Jute & Mesta_bubble.png
│  │  │  ├─ Jute & Mesta_Production_Yield.png
│  │  │  ├─ Jute_Area_Production.png
│  │  │  ├─ Jute_Area_Yield.png
│  │  │  ├─ Jute_bubble.png
│  │  │  ├─ Jute_Production_Yield.png
│  │  │  ├─ Linseed_Area_Production.png
│  │  │  ├─ Linseed_Area_Yield.png
│  │  │  ├─ Linseed_bubble.png
│  │  │  ├─ Linseed_Production_Yield.png
│  │  │  ├─ Maize_Area_Production.png
│  │  │  ├─ Maize_Area_Yield.png
│  │  │  ├─ Maize_bubble.png
│  │  │  ├─ Maize_Production_Yield.png
│  │  │  ├─ Mesta_Area_Production.png
│  │  │  ├─ Mesta_Area_Yield.png
│  │  │  ├─ Mesta_bubble.png
│  │  │  ├─ Mesta_Production_Yield.png
│  │  │  ├─ Niger seed_Area_Production.png
│  │  │  ├─ Niger seed_Area_Yield.png
│  │  │  ├─ Niger seed_bubble.png
│  │  │  ├─ Niger seed_Production_Yield.png
│  │  │  ├─ Nine Oilseeds_Area_Production.png
│  │  │  ├─ Nine Oilseeds_Area_Yield.png
│  │  │  ├─ Nine Oilseeds_bubble.png
│  │  │  ├─ Nine Oilseeds_Production_Yield.png
│  │  │  ├─ Onion_Area_Production.png
│  │  │  ├─ Onion_Area_Yield.png
│  │  │  ├─ Onion_bubble.png
│  │  │  ├─ Onion_Production_Yield.png
│  │  │  ├─ Other Pulses_Area_Production.png
│  │  │  ├─ Other Pulses_Area_Yield.png
│  │  │  ├─ Other Pulses_bubble.png
│  │  │  ├─ Other Pulses_Production_Yield.png
│  │  │  ├─ Potato_Area_Production.png
│  │  │  ├─ Potato_Area_Yield.png
│  │  │  ├─ Potato_bubble.png
│  │  │  ├─ Potato_Production_Yield.png
│  │  │  ├─ Ragi_Area_Production.png
│  │  │  ├─ Ragi_Area_Yield.png
│  │  │  ├─ Ragi_bubble.png
│  │  │  ├─ Ragi_Production_Yield.png
│  │  │  ├─ Rapeseed & Mustard_Area_Production.png
│  │  │  ├─ Rapeseed & Mustard_Area_Yield.png
│  │  │  ├─ Rapeseed & Mustard_bubble.png
│  │  │  ├─ Rapeseed & Mustard_Production_Yield.png
│  │  │  ├─ Rice_Area_Production.png
│  │  │  ├─ Rice_Area_Yield.png
│  │  │  ├─ Rice_bubble.png
│  │  │  ├─ Rice_Production_Yield.png
│  │  │  ├─ Rubber_Area_Production.png
│  │  │  ├─ Rubber_Area_Yield.png
│  │  │  ├─ Rubber_bubble.png
│  │  │  ├─ Rubber_Production_Yield.png
│  │  │  ├─ Safflower_Area_Production.png
│  │  │  ├─ Safflower_Area_Yield.png
│  │  │  ├─ Safflower_bubble.png
│  │  │  ├─ Safflower_Production_Yield.png
│  │  │  ├─ Sannhamp_Area_Production.png
│  │  │  ├─ Sannhamp_Area_Yield.png
│  │  │  ├─ Sannhamp_bubble.png
│  │  │  ├─ Sannhamp_Production_Yield.png
│  │  │  ├─ Sesamum_Area_Production.png
│  │  │  ├─ Sesamum_Area_Yield.png
│  │  │  ├─ Sesamum_bubble.png
│  │  │  ├─ Sesamum_Production_Yield.png
│  │  │  ├─ Small millets_Area_Production.png
│  │  │  ├─ Small millets_Area_Yield.png
│  │  │  ├─ Small millets_bubble.png
│  │  │  ├─ Small millets_Production_Yield.png
│  │  │  ├─ Soyabean_Area_Production.png
│  │  │  ├─ Soyabean_Area_Yield.png
│  │  │  ├─ Soyabean_bubble.png
│  │  │  ├─ Soyabean_Production_Yield.png
│  │  │  ├─ Sugarcane_Area_Production.png
│  │  │  ├─ Sugarcane_Area_Yield.png
│  │  │  ├─ Sugarcane_bubble.png
│  │  │  ├─ Sugarcane_Production_Yield.png
│  │  │  ├─ Sunflower_Area_Production.png
│  │  │  ├─ Sunflower_Area_Yield.png
│  │  │  ├─ Sunflower_bubble.png
│  │  │  ├─ Sunflower_Production_Yield.png
│  │  │  ├─ Sweet potato_Area_Production.png
│  │  │  ├─ Sweet potato_Area_Yield.png
│  │  │  ├─ Sweet potato_bubble.png
│  │  │  ├─ Sweet potato_Production_Yield.png
│  │  │  ├─ Tapioca_Area_Production.png
│  │  │  ├─ Tapioca_Area_Yield.png
│  │  │  ├─ Tapioca_bubble.png
│  │  │  ├─ Tapioca_Production_Yield.png
│  │  │  ├─ Tea_Area_Production.png
│  │  │  ├─ Tea_Area_Yield.png
│  │  │  ├─ Tea_bubble.png
│  │  │  ├─ Tea_Production_Yield.png
│  │  │  ├─ Tobacco_Area_Production.png
│  │  │  ├─ Tobacco_Area_Yield.png
│  │  │  ├─ Tobacco_bubble.png
│  │  │  ├─ Tobacco_Production_Yield.png
│  │  │  ├─ Total Fibers_Area_Production.png
│  │  │  ├─ Total Fibers_Area_Yield.png
│  │  │  ├─ Total Fibers_bubble.png
│  │  │  ├─ Total Fibers_Production_Yield.png
│  │  │  ├─ Total Foodgrains_Area_Production.png
│  │  │  ├─ Total Foodgrains_Area_Yield.png
│  │  │  ├─ Total Foodgrains_bubble.png
│  │  │  ├─ Total Foodgrains_Production_Yield.png
│  │  │  ├─ Total Fruits & Vegetables_Area_Production.png
│  │  │  ├─ Total Fruits & Vegetables_Area_Yield.png
│  │  │  ├─ Total Fruits & Vegetables_bubble.png
│  │  │  ├─ Total Fruits & Vegetables_Production_Yield.png
│  │  │  ├─ Total Non-Food grains_Area_Production.png
│  │  │  ├─ Total Non-Food grains_Area_Yield.png
│  │  │  ├─ Total Non-Food grains_bubble.png
│  │  │  ├─ Total Non-Food grains_Production_Yield.png
│  │  │  ├─ Total Oilseeds_Area_Production.png
│  │  │  ├─ Total Oilseeds_Area_Yield.png
│  │  │  ├─ Total Oilseeds_bubble.png
│  │  │  ├─ Total Oilseeds_Production_Yield.png
│  │  │  ├─ Total Pulses_Area_Production.png
│  │  │  ├─ Total Pulses_Area_Yield.png
│  │  │  ├─ Total Pulses_bubble.png
│  │  │  ├─ Total Pulses_Production_Yield.png
│  │  │  ├─ Total Spices_Area_Production.png
│  │  │  ├─ Total Spices_Area_Yield.png
│  │  │  ├─ Total Spices_bubble.png
│  │  │  ├─ Total Spices_Production_Yield.png
│  │  │  ├─ Turmeric_Area_Production.png
│  │  │  ├─ Turmeric_Area_Yield.png
│  │  │  ├─ Turmeric_bubble.png
│  │  │  ├─ Turmeric_Production_Yield.png
│  │  │  ├─ Wheat_Area_Production.png
│  │  │  ├─ Wheat_Area_Yield.png
│  │  │  ├─ Wheat_bubble.png
│  │  │  ├─ Wheat_Production_Yield.png
│  │  │  ├─ Yield for Crop ARHAR.png
│  │  │  ├─ Yield for Crop COTTON.png
│  │  │  ├─ Yield for Crop GRAM.png
│  │  │  ├─ Yield for Crop GROUNDNUT.png
│  │  │  ├─ Yield for Crop MAIZE.png
│  │  │  ├─ Yield for Crop MOONG.png
│  │  │  ├─ Yield for Crop PADDY.png
│  │  │  ├─ Yield for Crop RAPESEED AND MUSTARD.png
│  │  │  ├─ Yield for Crop SUGARCANE.png
│  │  │  ├─ Yield for Crop WHEAT.png
│  │  │  ├─ Yield for State Andhra Pradesh.png
│  │  │  ├─ Yield for State Bihar.png
│  │  │  ├─ Yield for State Gujarat.png
│  │  │  ├─ Yield for State Haryana.png
│  │  │  ├─ Yield for State Karnataka.png
│  │  │  ├─ Yield for State Madhya Pradesh.png
│  │  │  ├─ Yield for State Maharashtra.png
│  │  │  ├─ Yield for State Orissa.png
│  │  │  ├─ Yield for State Punjab.png
│  │  │  ├─ Yield for State Rajasthan.png
│  │  │  ├─ Yield for State Tamil Nadu.png
│  │  │  ├─ Yield for State Uttar Pradesh.png
│  │  │  └─ Yield for State West Bengal.png
│  │  ├─ js
│  │  └─ plugins
│  │     └─ bootstrap
│  │        ├─ css
│  │        │  ├─ bootstrap-grid.css
│  │        │  ├─ bootstrap-grid.css.map
│  │        │  ├─ bootstrap-grid.min.css
│  │        │  ├─ bootstrap-grid.min.css.map
│  │        │  ├─ bootstrap-grid.rtl.css
│  │        │  ├─ bootstrap-grid.rtl.css.map
│  │        │  ├─ bootstrap-grid.rtl.min.css
│  │        │  ├─ bootstrap-grid.rtl.min.css.map
│  │        │  ├─ bootstrap-reboot.css
│  │        │  ├─ bootstrap-reboot.css.map
│  │        │  ├─ bootstrap-reboot.min.css
│  │        │  ├─ bootstrap-reboot.min.css.map
│  │        │  ├─ bootstrap-reboot.rtl.css
│  │        │  ├─ bootstrap-reboot.rtl.css.map
│  │        │  ├─ bootstrap-reboot.rtl.min.css
│  │        │  ├─ bootstrap-reboot.rtl.min.css.map
│  │        │  ├─ bootstrap-utilities.css
│  │        │  ├─ bootstrap-utilities.css.map
│  │        │  ├─ bootstrap-utilities.min.css
│  │        │  ├─ bootstrap-utilities.min.css.map
│  │        │  ├─ bootstrap-utilities.rtl.css
│  │        │  ├─ bootstrap-utilities.rtl.css.map
│  │        │  ├─ bootstrap-utilities.rtl.min.css
│  │        │  ├─ bootstrap-utilities.rtl.min.css.map
│  │        │  ├─ bootstrap.css
│  │        │  ├─ bootstrap.css.map
│  │        │  ├─ bootstrap.min.css
│  │        │  ├─ bootstrap.min.css.map
│  │        │  ├─ bootstrap.rtl.css
│  │        │  ├─ bootstrap.rtl.css.map
│  │        │  ├─ bootstrap.rtl.min.css
│  │        │  └─ bootstrap.rtl.min.css.map
│  │        └─ js
│  │           ├─ bootstrap.bundle.js
│  │           ├─ bootstrap.bundle.js.map
│  │           ├─ bootstrap.bundle.min.js
│  │           ├─ bootstrap.bundle.min.js.map
│  │           ├─ bootstrap.esm.js
│  │           ├─ bootstrap.esm.js.map
│  │           ├─ bootstrap.esm.min.js
│  │           ├─ bootstrap.esm.min.js.map
│  │           ├─ bootstrap.js
│  │           ├─ bootstrap.js.map
│  │           ├─ bootstrap.min.js
│  │           └─ bootstrap.min.js.map
│  ├─ templates
│  │  ├─ Area_Production.html
│  │  ├─ Area_Yield.html
│  │  ├─ Bubble.html
│  │  ├─ Cost_analysis_ARHAR.html
│  │  ├─ Cost_analysis_COTTON.html
│  │  ├─ Cost_analysis_GRAM.html
│  │  ├─ Cost_analysis_GROUNGNUT.html
│  │  ├─ Cost_analysis_MAIZE.html
│  │  ├─ Cost_analysis_MOONG.html
│  │  ├─ Cost_analysis_PADDY.html
│  │  ├─ Cost_analysis_RAPESEED.html
│  │  ├─ Cost_analysis_SUGARCANE.html
│  │  ├─ Cost_analysis_WHEAT.html
│  │  ├─ Cost_Cultivation_Crop_ARHAR.html
│  │  ├─ Cost_Cultivation_Crop_COTTON.html
│  │  ├─ Cost_Cultivation_Crop_GRAM.html
│  │  ├─ Cost_Cultivation_Crop_GROUNDNUT.html
│  │  ├─ Cost_Cultivation_Crop_MAIZE.html
│  │  ├─ Cost_Cultivation_Crop_MOONG.html
│  │  ├─ Cost_Cultivation_Crop_PADDY.html
│  │  ├─ Cost_Cultivation_Crop_RAPESEED.html
│  │  ├─ Cost_Cultivation_Crop_SUGARCANE.html
│  │  ├─ Cost_Cultivation_Crop_WHEAT.html
│  │  ├─ Cost_Cultivation_State_Andhra_Pradesh.html
│  │  ├─ Cost_Cultivation_State_Bihar.html
│  │  ├─ Cost_Cultivation_State_Gujarat.html
│  │  ├─ Cost_Cultivation_State_Haryana.html
│  │  ├─ Cost_Cultivation_State_Karnataka.html
│  │  ├─ Cost_Cultivation_State_Madhya_Pradesh.html
│  │  ├─ Cost_Cultivation_State_Maharashtra.html
│  │  ├─ Cost_Cultivation_State_Orissa.html
│  │  ├─ Cost_Cultivation_State_Punjab.html
│  │  ├─ Cost_Cultivation_State_Rajasthan.html
│  │  ├─ Cost_Cultivation_State_Tamil_Nadu.html
│  │  ├─ Cost_Cultivation_State_Uttar_Pradesh.html
│  │  ├─ Cost_Cultivation_State_West_Bengal.html
│  │  ├─ Cost_Production_Crop_ARHAR.html
│  │  ├─ Cost_Production_Crop_COTTON.html
│  │  ├─ Cost_Production_Crop_GRAM.html
│  │  ├─ Cost_Production_Crop_GROUNDNUT.html
│  │  ├─ Cost_Production_Crop_MAIZE.html
│  │  ├─ Cost_Production_Crop_MOONG.html
│  │  ├─ Cost_Production_Crop_PADDY.html
│  │  ├─ Cost_Production_Crop_RAPESEED.html
│  │  ├─ Cost_Production_Crop_SUGARCANE.html
│  │  ├─ Cost_Production_Crop_WHEAT.html
│  │  ├─ Cost_Production_State_Andhra_Pradesh.html
│  │  ├─ Cost_Production_State_Bihar.html
│  │  ├─ Cost_Production_State_Gujarat.html
│  │  ├─ Cost_Production_State_Haryana.html
│  │  ├─ Cost_Production_State_Karnataka.html
│  │  ├─ Cost_Production_State_Madhya_Pradesh.html
│  │  ├─ Cost_Production_State_Maharashtra.html
│  │  ├─ Cost_Production_State_Orissa.html
│  │  ├─ Cost_Production_State_Punjab.html
│  │  ├─ Cost_Production_State_Rajasthan.html
│  │  ├─ Cost_Production_State_Tamil_Nadu.html
│  │  ├─ Cost_Production_State_Uttar_Pradesh.html
│  │  ├─ Cost_Production_State_West_Bengal.html
│  │  ├─ Home.html
│  │  ├─ layout.html
│  │  ├─ Production_Yield.html
│  │  ├─ Yield_Crop_ARHAR.html
│  │  ├─ Yield_Crop_COTTON.html
│  │  ├─ Yield_Crop_GRAM.html
│  │  ├─ Yield_Crop_GROUNDNUT.html
│  │  ├─ Yield_Crop_MAIZE.html
│  │  ├─ Yield_Crop_MOONG.html
│  │  ├─ Yield_Crop_PADDY.html
│  │  ├─ Yield_Crop_RAPESEED.html
│  │  ├─ Yield_Crop_SUGARCANE.html
│  │  ├─ Yield_Crop_WHEAT.html
│  │  ├─ Yield_State_Andhra_Pradesh.html
│  │  ├─ Yield_State_Bihar.html
│  │  ├─ Yield_State_Gujarat.html
│  │  ├─ Yield_State_Haryana.html
│  │  ├─ Yield_State_Karnataka.html
│  │  ├─ Yield_State_Madhya_Pradesh.html
│  │  ├─ Yield_State_Maharashtra.html
│  │  ├─ Yield_State_Orissa.html
│  │  ├─ Yield_State_Punjab.html
│  │  ├─ Yield_State_Rajasthan.html
│  │  ├─ Yield_State_Tamil_Nadu.html
│  │  ├─ Yield_State_Uttar_Pradesh.html
│  │  └─ Yield_State_West_Bengal.html
│  ├─ tests.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-39.pyc
│     ├─ apps.cpython-39.pyc
│     ├─ models.cpython-39.pyc
│     ├─ views.cpython-39.pyc
│     └─ __init__.cpython-39.pyc
├─ dashboard
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ settings.cpython-39.pyc
│     ├─ urls.cpython-39.pyc
│     ├─ wsgi.cpython-39.pyc
│     └─ __init__.cpython-39.pyc
├─ db.sqlite3
└─ manage.py

2. Exploratory data analysis.ipynb
3. datafile (1).csv
4. datafile (2).csv
5. Maintenance Manual.pdf

Dependencies:
-------------
- Python 3.9+
- Any modern PC (min. 2 GB RAM, 2-core processor)
- Disk Space: At least 200MB free for project and datasets

How to Run:
-----------
1. Clone the repository using the command: 'git clone https://github.com/TSY648/Data-visualisation-dashboard-for-agricultural-land-management.git'
2. Start server by using the command: 'python manage.py runserver'
3. Open browser by clicking the appeared link: 'http://127.0.0.1:8000/'
4. Type '/home/' after the link to enter the home page.
5. Use different buttons on the dashboard to switch between different visual images.
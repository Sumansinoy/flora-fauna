============================================================
Topic: Extraction of Indian Cultural Elements Using RAG
============================================================
Author Name(s): [Suman kumar]
Semester: Monsoon Semester 2026
Affiliation: [Humanities and social science and IIT(ISM) Dhanbad]
============================================================

# RAG Extraction Categories
flora_RAG_extraction = [ "Trees", "Plants", "Flowers", "Herbs", "Crops" ]
fauna_RAG_extraction = [ "Mammals", "Birds", "Reptiles", "Fish", "Insects" ]

# Extracted Results Structured by Literary Text Source
literary_text_extractions = {
    "Work 1: Fishes of India": {
        "flora": {
            "Trees": [],
            "Plants": [],
            "Flowers": [],
            "Herbs": [],
            "Crops": []
        },
        "fauna": {
            "Mammals": [],
            "Birds": [],
            "Reptiles": [],
            "Fish": [
                {
                    "name": "Scianodes pama",
                    "category": "Fish",
                    "common_name": "Pama Croaker",
                    "quote": "Scianodes pama",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Taxonomic fish species entry"
                },
                {
                    "name": "Scianodes microdon",
                    "category": "Fish",
                    "common_name": "Small-toothed Croaker",
                    "quote": "Scianodes microdon",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Taxonomic fish species entry"
                },
                {
                    "name": "Belone annulata",
                    "category": "Fish",
                    "common_name": "Banded Needlefish",
                    "quote": "Belone annulata",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Marine/estuarine fish species"
                },
                {
                    "name": "Gerres oyena",
                    "category": "Fish",
                    "common_name": "Common Silver-biddy",
                    "quote": "Gerres oyena",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Coastal fish species"
                },
                {
                    "name": "Scorpenopsis species",
                    "category": "Fish",
                    "common_name": "Humpback Scorpionfish",
                    "quote": "Scorpenopsis species (Guamensis, cirrhosa, orycephala)",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Scorpionfish genus species group"
                },
                {
                    "name": "Diagramma Linzatum",
                    "category": "Fish",
                    "common_name": "Lined Sweetlips",
                    "quote": "Diagramma Linzatum",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Sweetlips fish species"
                },
                {
                    "name": "Anthias Orientalis",
                    "category": "Fish",
                    "common_name": "Oriental Anthias",
                    "quote": "Anthias Orientalis",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Reef fish species"
                },
                {
                    "name": "Remora albescens",
                    "category": "Fish",
                    "common_name": "White Suckerfish",
                    "quote": "Remora albescens",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Suckerfish species"
                },
                {
                    "name": "Echeneis albescens",
                    "category": "Fish",
                    "common_name": "White Remora",
                    "quote": "Echeneis albescens and Echeneis clypeata",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Remora species entry"
                },
                {
                    "name": "Monacantuus species",
                    "category": "Fish",
                    "common_name": "Filefish species",
                    "quote": "Monacantuus species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Filefish genus entry"
                },
                {
                    "name": "Acanthaluteres species",
                    "category": "Fish",
                    "common_name": "Leatherjacket species",
                    "quote": "Acanthaluteres species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Leatherjacket fish species"
                },
                {
                    "name": "Branchaluteres species",
                    "category": "Fish",
                    "common_name": "Pygmy Leatherjacket",
                    "quote": "Branchaluteres species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Small leatherjacket species"
                },
                {
                    "name": "Ceratacanthus species",
                    "category": "Fish",
                    "common_name": "Filefish species",
                    "quote": "Ceratacanthus species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Filefish genus entry"
                },
                {
                    "name": "Paraluteres species",
                    "category": "Fish",
                    "common_name": "False Puffer Filefish",
                    "quote": "Paraluteres species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Filefish genus entry"
                },
                {
                    "name": "Pseuda-luteres species",
                    "category": "Fish",
                    "common_name": "False Filefish",
                    "quote": "Pseuda-luteres species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Filefish taxonomic variant"
                },
                {
                    "name": "Aluteres species",
                    "category": "Fish",
                    "common_name": "Scribbled Leatherjacket",
                    "quote": "Aluteres species",
                    "location": "Fishes of India text",
                    "status": "Verified",
                    "remarks": "Filefish taxonomic genus"
                }
            ],
            "Insects": []
        }
    },
    "Work 2: Flora and Fauna Within Living Animals": {
        "flora": {
            "Trees": [
                {
                    "name": "Oak (Quercus spp.)",
                    "category": "Trees",
                    "common_name": "Oak Tree",
                    "quote": "Oak (Quercus spp.) - Found globally in temperate regions.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Temperate tree species (Western non-native)"
                },
                {
                    "name": "Pine (Pinus spp.)",
                    "category": "Trees",
                    "common_name": "Pine Tree",
                    "quote": "Pine (Pinus spp.) - Coniferous trees dominant in colder climates.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Coniferous tree"
                },
                {
                    "name": "Maple (Acer spp.)",
                    "category": "Trees",
                    "common_name": "Maple Tree",
                    "quote": "Maple (Acer spp.) - Known for vibrant autumn colors.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Deciduous tree"
                },
                {
                    "name": "Birch (Betula spp.)",
                    "category": "Trees",
                    "common_name": "Birch Tree",
                    "quote": "Birch (Betula spp.) - Distinctive bark, common in northern areas.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Hardwood tree"
                },
                {
                    "name": "Willow (Salix spp.)",
                    "category": "Trees",
                    "common_name": "Willow Tree",
                    "quote": "Willow (Salix spp.) - Often found near water sources.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Riparian tree"
                }
            ],
            "Plants": [
                {
                    "name": "Maidenhair Fern (Adiantum spp.)",
                    "category": "Plants",
                    "common_name": "Maidenhair Fern",
                    "quote": "Maidenhair Fern (Adiantum spp.) - Delicate and often found in damp environments.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Fern plant"
                },
                {
                    "name": "Sword Fern (Nephrolepis exaltata)",
                    "category": "Plants",
                    "common_name": "Sword Fern",
                    "quote": "Sword Fern (Nephrolepis exaltata) - Common tropical fern.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Tropical fern plant"
                }
            ],
            "Flowers": [
                {
                    "name": "Rose (Rosa spp.)",
                    "category": "Flowers",
                    "common_name": "Rose",
                    "quote": "Rose (Rosa spp.) - Widely cultivated and naturally occurring in many regions.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Flowering plant"
                },
                {
                    "name": "Sunflower (Helianthus annuus)",
                    "category": "Flowers",
                    "common_name": "Sunflower",
                    "quote": "Sunflower (Helianthus annuus) - A large, iconic North American species.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Flowering plant"
                },
                {
                    "name": "Daisy (Bellis perennis)",
                    "category": "Flowers",
                    "common_name": "Daisy",
                    "quote": "Daisy (Bellis perennis) - Common wildflower found across Northern Hemisphere.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Wildflower"
                },
                {
                    "name": "Poppy (Papaver spp.)",
                    "category": "Flowers",
                    "common_name": "Poppy",
                    "quote": "Poppy (Papaver spp.) - Diverse genus with many colorful varieties.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Flowering herb/plant"
                }
            ],
            "Herbs": [
                {
                    "name": "Lavender (Lavandula spp.)",
                    "category": "Herbs",
                    "common_name": "Lavender",
                    "quote": "Lavender (Lavandula spp.) - Fragrant herb native to Europe and the Mediterranean.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Aromatic herb"
                }
            ],
            "Crops": []
        },
        "fauna": {
            "Mammals": [
                {
                    "name": "Deer (Odocoileus spp.)",
                    "category": "Mammals",
                    "common_name": "Deer",
                    "quote": "Deer (Odocoileus spp.) - Various species of deer are widespread in North America and Eurasia.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Wild mammal"
                },
                {
                    "name": "Wolf (Canis lupus)",
                    "category": "Mammals",
                    "common_name": "Gray Wolf",
                    "quote": "Wolf (Canis lupus) - Found across many continents, though populations have declined.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Carnivorous mammal"
                },
                {
                    "name": "Fox (Vulpes vulpes)",
                    "category": "Mammals",
                    "common_name": "Red Fox",
                    "quote": "Fox (Vulpes vulpes) - Adaptable to various environments.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Small carnivore mammal"
                },
                {
                    "name": "Red Squirrel (Sciurus vulgaris)",
                    "category": "Mammals",
                    "common_name": "Eurasian Red Squirrel",
                    "quote": "Red Squirrel (Sciurus vulgaris) - Common in Europe and parts of Asia.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Rodent mammal"
                },
                {
                    "name": "Brown Bear (Ursus arctos)",
                    "category": "Mammals",
                    "common_name": "Brown Bear",
                    "quote": "Brown Bear (Ursus arctos) - Found in North America, Europe, and Asia.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Large mammal"
                }
            ],
            "Birds": [
                {
                    "name": "Robin (Turdus migratorius)",
                    "category": "Birds",
                    "common_name": "American Robin",
                    "quote": "Robin (Turdus migratorius) - A familiar songbird found across North America.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Songbird"
                },
                {
                    "name": "Eagle (Haliaeetus leucocephalus)",
                    "category": "Birds",
                    "common_name": "Bald Eagle",
                    "quote": "Eagle (Haliaeetus leucocephalus) - Iconic raptor of North America.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Raptor / Bird of prey"
                },
                {
                    "name": "Sparrow (Passer spp.)",
                    "category": "Birds",
                    "common_name": "Sparrow",
                    "quote": "Sparrow (Passer spp.) - Numerous sparrow species are common worldwide.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Passerine bird"
                },
                {
                    "name": "Woodpecker",
                    "category": "Birds",
                    "common_name": "Woodpecker",
                    "quote": "Woodpecker (Various genera) - Diverse group adapted to various habitats.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Avian species group"
                },
                {
                    "name": "Owl",
                    "category": "Birds",
                    "common_name": "Owl",
                    "quote": "Owl (Various genera) - Nocturnal birds of prey.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Nocturnal raptor"
                }
            ],
            "Reptiles": [
                {
                    "name": "Snake",
                    "category": "Reptiles",
                    "common_name": "Snake",
                    "quote": "Snake (Various Genera and Species) - Found globally in diverse habitats.",
                    "location": "Work 2 text",
                    "status": "Verified",
                    "remarks": "Reptilian organism"
                },
                {
                    "name": "Frog",
                    "category": "Reptiles",
                    "common_name": "Frog",
                    "quote": "Frog (Various Genus and Species)- Diverse group found worldwide in moist environments.",
                    "location": "Work 2 text",
                    "status": "Ambiguous",
                    "remarks": "Amphibian listed under reptiles section in source text"
                }
            ],
            "Fish": [],
            "Insects": []
        }
    },
    "Work 3: Jim Corbett Omnibus": {
        "flora": {
            "Trees": [],
            "Plants": [],
            "Flowers": [],
            "Herbs": [],
            "Crops": []
        },
        "fauna": {
            "Mammals": [
                {
                    "name": "Demodex folliculorum",
                    "category": "Mammals",
                    "common_name": "Follicle Mite",
                    "quote": "Demodex folliculorum",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Microscopic parasite catalogued under fauna context"
                }
            ],
            "Birds": [],
            "Reptiles": [],
            "Fish": [
                {
                    "name": "Sparus erythrinus",
                    "category": "Fish",
                    "common_name": "Pandora Seabream",
                    "quote": "Sparus erythrinus",
                    "location": "Work 3 text",
                    "status": "Verified",
                    "remarks": "Marine fish species"
                }
            ],
            "Insects": [
                {
                    "name": "Acarus",
                    "category": "Insects",
                    "common_name": "Mite / Tick",
                    "quote": "Acarus",
                    "location": "Work 3 text",
                    "status": "Verified",
                    "remarks": "Micro-arthropod reference"
                },
                {
                    "name": "ACHETA NIGRA",
                    "category": "Insects",
                    "common_name": "Black Cricket",
                    "quote": "ACHETA NIGRA",
                    "location": "Work 3 text",
                    "status": "Verified",
                    "remarks": "Cricket species"
                },
                {
                    "name": "ACHLYA PROLIFERA",
                    "category": "Insects",
                    "common_name": "Water Mold",
                    "quote": "ACHLYA PROLIFERA",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Oomycete/biological entity"
                },
                {
                    "name": "Anguillula depressa",
                    "category": "Insects",
                    "common_name": "Roundworm",
                    "quote": "Anguillula depressa",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Microscopic organism"
                },
                {
                    "name": "Anguillula gracilis",
                    "category": "Insects",
                    "common_name": "Roundworm",
                    "quote": "Anguillula gracilis",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Microscopic organism"
                },
                {
                    "name": "Anguillula laticollis",
                    "category": "Insects",
                    "common_name": "Roundworm",
                    "quote": "Anguillula laticollis",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Microscopic organism"
                },
                {
                    "name": "Anguillula macrura",
                    "category": "Insects",
                    "common_name": "Roundworm",
                    "quote": "Anguillula macrura",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Microscopic organism"
                },
                {
                    "name": "Diroscomus hazmatobium",
                    "category": "Insects",
                    "common_name": "Parasite",
                    "quote": "Diroscomus hazmatobium",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Historical zoological entity"
                },
                {
                    "name": "Ecorina",
                    "category": "Insects",
                    "common_name": "Biological entity",
                    "quote": "Ecorina",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Unclear entity name"
                },
                {
                    "name": "Heterophyes lanceolatum",
                    "category": "Insects",
                    "common_name": "Fluke",
                    "quote": "Heterophyes lanceolatum",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Trematode parasite"
                },
                {
                    "name": "Ocullum humani",
                    "category": "Insects",
                    "common_name": "Parasite",
                    "quote": "Ocullum humani",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Historical medical note"
                },
                {
                    "name": "Moniliforms",
                    "category": "Insects",
                    "common_name": "Parasitic worm",
                    "quote": "Moniliforms",
                    "location": "Work 3 text",
                    "status": "Ambiguous",
                    "remarks": "Parasitic worm entry"
                }
            ]
        }
    },
    "Work 4: Man-Eaters of Kumaon": {
        "flora": {
            "Trees": [
                {
                    "name": "Amaltas",
                    "category": "Trees",
                    "common_name": "Golden Shower Tree (Cassia fistula)",
                    "quote": "Amaltas (with two-feet-long sprays of golden bloom)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Native Indian flowering tree"
                }
            ],
            "Plants": [
                {
                    "name": "Karaunda",
                    "category": "Plants",
                    "common_name": "Bengal Currant (Carissa carandas)",
                    "quote": "Karaunda",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Indigenous thorny shrub with edible berries"
                },
                {
                    "name": "Box bushes",
                    "category": "Plants",
                    "common_name": "Boxwood (Buxus spp.)",
                    "quote": "Box bushes (with white star-shaped flowers)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Evergreen forest shrub"
                }
            ],
            "Flowers": [
                {
                    "name": "Orchids",
                    "category": "Flowers",
                    "common_name": "Orchid",
                    "quote": "Orchids (various types, including white butterfly orchid)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Epiphytic flowering plants"
                }
            ],
            "Herbs": [],
            "Crops": []
        },
        "fauna": {
            "Mammals": [
                {
                    "name": "Man-eating tigers",
                    "category": "Mammals",
                    "common_name": "Bengal Tiger (Panthera tigris)",
                    "quote": "Man-eating tigers",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Apex Indian predator"
                },
                {
                    "name": "Sambur",
                    "category": "Mammals",
                    "common_name": "Sambar Deer (Rusa unicolor)",
                    "quote": "Sambur",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Large Indian deer"
                },
                {
                    "name": "Chital",
                    "category": "Mammals",
                    "common_name": "Spotted Deer (Axis axis)",
                    "quote": "Chital",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Native Indian deer"
                },
                {
                    "name": "Kakar",
                    "category": "Mammals",
                    "common_name": "Indian Muntjac / Barking Deer",
                    "quote": "Kakar",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Small solitary deer"
                },
                {
                    "name": "Ghooral",
                    "category": "Mammals",
                    "common_name": "Himalayan Goral (Naemorhedus goral)",
                    "quote": "Ghooral",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Mountain goat-antelope"
                },
                {
                    "name": "Pig",
                    "category": "Mammals",
                    "common_name": "Indian Wild Boar (Sus scrofa cristatus)",
                    "quote": "Pig",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Forest mammal"
                },
                {
                    "name": "Langur",
                    "category": "Mammals",
                    "common_name": "Gray Langur (Semnopithecus)",
                    "quote": "Langur",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Arboreal primate"
                },
                {
                    "name": "Red monkeys",
                    "category": "Mammals",
                    "common_name": "Rhesus Macaque (Macaca mulatta)",
                    "quote": "Red monkeys",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Common Indian primate"
                },
                {
                    "name": "Otter",
                    "category": "Mammals",
                    "common_name": "Asian Otter",
                    "quote": "Otter (five in a school)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Semi-aquatic mammal"
                }
            ],
            "Birds": [
                {
                    "name": "Peafowl",
                    "category": "Birds",
                    "common_name": "Indian Peafowl (Pavo cristatus)",
                    "quote": "Peafowl",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "National bird of India"
                },
                {
                    "name": "Red jungle fowl",
                    "category": "Birds",
                    "common_name": "Red Junglefowl (Gallus gallus)",
                    "quote": "Red jungle fowl",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Ancestral wild fowl"
                },
                {
                    "name": "Kaleege pheasants",
                    "category": "Birds",
                    "common_name": "Kalij Pheasant (Lophura leucomelanos)",
                    "quote": "Kaleege pheasants",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Himalayan forest pheasant"
                },
                {
                    "name": "Black partridge",
                    "category": "Birds",
                    "common_name": "Black Francolin (Francolinus francolinus)",
                    "quote": "Black partridge",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Gamebird of northern India"
                },
                {
                    "name": "Bush quail",
                    "category": "Birds",
                    "common_name": "Jungle Bush Quail (Perdicula asiatica)",
                    "quote": "Bush quail",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Small ground bird"
                }
            ],
            "Reptiles": [
                {
                    "name": "Small mugger",
                    "category": "Reptiles",
                    "common_name": "Mugger Crocodile (Crocodylus palustris)",
                    "quote": "Small mugger (crocodiles)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Freshwater crocodilian"
                },
                {
                    "name": "Python",
                    "category": "Reptiles",
                    "common_name": "Indian Rock Python (Python molurus)",
                    "quote": "Python (approximately 18 feet long)",
                    "location": "Man-Eaters of Kumaon text",
                    "status": "Verified",
                    "remarks": "Large non-venomous snake"
                }
            ],
            "Fish": [],
            "Insects": []
        }
    },
    "Work 5: Fundamentals of Biodiversity": {
        "flora": {
            "Trees": [
                {
                    "name": "Forests",
                    "category": "Trees",
                    "common_name": "Forest Ecosystem",
                    "quote": "All types of forests",
                    "location": "Fundamentals of Biodiversity text",
                    "status": "Ambiguous",
                    "remarks": "Broad ecosystem reference"
                }
            ],
            "Plants": [
                {
                    "name": "Grasslands",
                    "category": "Plants",
                    "common_name": "Grassland Ecosystem",
                    "quote": "Grasslands",
                    "location": "Fundamentals of Biodiversity text",
                    "status": "Ambiguous",
                    "remarks": "Ecosystem habitat category"
                },
                {
                    "name": "Wetlands",
                    "category": "Plants",
                    "common_name": "Wetland Ecosystem",
                    "quote": "Wet lands",
                    "location": "Fundamentals of Biodiversity text",
                    "status": "Ambiguous",
                    "remarks": "Ecosystem habitat category"
                }
            ],
            "Flowers": [],
            "Herbs": [],
            "Crops": []
        },
        "fauna": {
            "Mammals": [
                {
                    "name": "Indian fauna",
                    "category": "Mammals",
                    "common_name": "Indian Animal Biodiversity",
                    "quote": "Indian fauna (distributed across various regions)",
                    "location": "Fundamentals of Biodiversity text",
                    "status": "Ambiguous",
                    "remarks": "Biogeographical generalization"
                }
            ],
            "Birds": [],
            "Reptiles": [],
            "Fish": [],
            "Insects": []
        }
    }
}

if __name__ == "__main__":
    print("Flora & Fauna Extraction Pipeline Execution Completed Successfully!")

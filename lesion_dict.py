lesion_dict = {'MEL': 'Melanoma (MEL), also known as malignant melanoma, is a type of skin cancer that develops from the pigment-producing cells known as melanocytes. Melanomas typically occur in the skin but may rarely occur in the mouth, intestines or eye (uveal melanoma) (WIKIPEDIA)',
               'NV': 'A melanocytic nevus (NV), also known as nevocytic nevus, nevus-cell nevus and commonly as a mole, is a type of melanocytic tumor that contains nevus cells. Some sources equate the term mole with "melanocytic nevus", but there are also sources that equate the term mole with any nevus form. (WIKIPEDIA)',
               'BCC': 'Basal-cell carcinoma (BCC), also known as basal-cell cancer, is the most common type of skin cancer. It often appears as a painless raised area of skin, which may be shiny with small blood vessels running over it. It may also present as a raised area with ulceration. (WIKIPEDIA)',
               'AK': 'Actinic keratosis (AK), sometimes called solar keratosis or senile keratosis, is a pre-cancerous area of thick, scaly, or crusty skin. The term actinic keratosis can be literally understood as a disorder (-osis) of epidermal keratinocytes that is induced by ultraviolet (UV) light exposure (actin-). (WIKIPEDIA)',
               'BKL': 'A seborrheic keratosis (or Benign keratosis - BK) is a non-cancerous (benign) skin tumour that originates from cells in the outer layer of the skin. Like liver spots, seborrheic keratoses are seen more often as people age. The tumours (also called lesions) appear in various colours, from light tan to black. (WIKIPEDIA)',
               'DF': 'Dermatofibromas (DF) are hard solitary slow-growing papules (rounded bumps) that may appear in a variety of colours, usually brownish to tan; they are often elevated or pedunculated. A dermatofibroma is associated with the dimple sign; by applying lateral pressure, there is a central depression of the dermatofibroma. (WIKIPEDIA)',
               'VASC': 'Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks (SSM Health)',
               'SCC': 'Squamous-cell skin cancer, also known as cutaneous squamous-cell carcinoma (SCC), is one of the main types of skin cancer along with basal cell cancer, and melanoma.It usually presents as a hard lump with a scaly top but can also form an ulcer. (WIKIPEDIA)',
               'UNK': 'This image does not fit into any of the above skin lesions. We are always updating so check back soon'
               }

lesion_urls = {'MEL': 'https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884',
               'NV': 'https://emedicine.medscape.com/article/1058445-overview',
               'BCC': 'https://www.mayoclinic.org/diseases-conditions/basal-cell-carcinoma/symptoms-causes/syc-20354187',
               'AK': 'https://www.mayoclinic.org/diseases-conditions/actinic-keratosis/symptoms-causes/syc-20354969',
               'BKL': 'https://www.mayoclinic.org/diseases-conditions/seborrheic-keratosis/symptoms-causes/syc-20353878',
               'DF': 'https://www.healthline.com/health/dermatofibromas',
               'VASC': 'https://www.ssmhealth.com/cardinal-glennon/pediatric-plastic-reconstructive-surgery/hemangiomas',
               'SCC': 'https://www.mayoclinic.org/diseases-conditions/squamous-cell-carcinoma/symptoms-causes/syc-20352480',
               'UNK': 'https://www.healthline.com/symptom/skin-lesion',
               }


def get_lesion_info(lesion, lesion_dict=lesion_dict):
    '''
    Get an overview of the type of lesion

    Input
    lesion: str - class of lesion
    lesion_dict: dict - dictionary of lesions and descriptions
    lesion_urls: dict - dictionary of lesions and urls for more information

    Output
    lesion_description: str - description of lesion type
    '''

    return lesion_dict[lesion], lesion_urls[lesion]

from flask import Flask, request, jsonify, render_template
from database import db, init_db
from models import Location
from flask_cors import CORS
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///safe_spaces.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)
sample_location = [
    {'id': 1, 'role': 'Software Engineer', 'company': 'Shopify', 'description': 'Must be willing to work long hours.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.04793119803071022, 'ageScore': 0.028574571013450623, 'feminineScore': 0.01503019966185093, 'masculineScore': 0.04793119803071022, 'racialScore': 0.009742510505020618, 'sexualityScore': 0.011159204877912998, 'disabilityScore': 0.03957347944378853
    },
    {'id': 2, 'role': 'Product Manager', 'company': 'Slack Technologies', 'description': 'Ideal for someone in the prime of their career.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Biased', 'score': 0.9270221590995789, 'ageScore': 0.9270221590995789, 'feminineScore': 0.08090150356292725, 'masculineScore': 0.046749673783779144, 'racialScore': 0.02520051598548889, 'sexualityScore': 0.03548639640212059, 'disabilityScore': 0.019359415397047997
    },
    {'id': 3, 'role': 'Data Scientist', 'company': 'Google', 'description': 'Work with large datasets to extract valuable insights.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.03528774902224541, 'ageScore': 0.01990361697971821, 'feminineScore': 0.01043853908777237, 'masculineScore': 0.026397421956062317, 'racialScore': 0.01009073480963707, 'sexualityScore': 0.009594270959496498, 'disabilityScore': 0.03528774902224541
    },
    {'id': 4, 'role': 'HR Manager', 'company': 'Deloitte', 'description': "Looking for a 'maverick' attitude", 'area': 'Mississauga', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.4639071822166443, 'ageScore': 0.10003755241632462, 'feminineScore': 0.01199291180819273, 'masculineScore': 0.4639071822166443, 'racialScore': 0.03055955283343792, 'sexualityScore': 0.021170806139707565, 'disabilityScore': 0.013417204841971397
    },
    {'id': 5, 'role': 'Marketing Specialist', 'company': 'RBC', 'description': 'Looking for someone who is self-sufficient and doesnt need guidance.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.43257349729537964, 'ageScore': 0.045012060552835464, 'feminineScore': 0.023006558418273926, 'masculineScore': 0.43257349729537964, 'racialScore': 0.019817154854536057, 'sexualityScore': 0.02582474611699581, 'disabilityScore': 0.05057312548160553
    },
    {'id': 6, 'role': 'UX Designer', 'company': 'Microsoft', 'description': 'Design user-friendly interfaces and experiences.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.017156602814793587, 'ageScore': 0.017156602814793587, 'feminineScore': 0.011673271656036377, 'masculineScore': 0.011922068893909454, 'racialScore': 0.011830734089016914, 'sexualityScore': 0.012330901809036732, 'disabilityScore': 0.016898078843951225
    },
    {'id': 7, 'role': 'Full Stack Developer', 'company': 'TD Bank', 'description': 'Looking for someone to work in a bro culture.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Biased', 'score': 0.7541272044181824, 'ageScore': 0.07084567099809647, 'feminineScore': 0.010158690623939037, 'masculineScore': 0.4115312099456787, 'racialScore': 0.02730671875178814, 'sexualityScore': 0.7541272044181824, 'disabilityScore': 0.018514027819037437
    },
    {'id': 8, 'role': 'Sales Executive', 'company': 'Bell Canada', 'description': 'Ideal candidate has a strong sense of authority.', 'area': 'Hamilton', 'location': 'Canada', 'label': 'Biased', 'score': 0.8827279806137085, 'ageScore': 0.040280330926179886, 'feminineScore': 0.018056903034448624, 'masculineScore': 0.8827279806137085, 'racialScore': 0.029745327308773994, 'sexualityScore': 0.02947937324643135, 'disabilityScore': 0.04355008155107498
    },
    {'id': 9, 'role': 'Software Architect', 'company': 'Intel', 'description': 'No drama allowed.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.024492457509040833, 'ageScore': 0.024492457509040833, 'feminineScore': 0.008920240215957165, 'masculineScore': 0.01885261759161949, 'racialScore': 0.010611096397042274, 'sexualityScore': 0.0114130275323987, 'disabilityScore': 0.015213320031762123
    },
    {'id': 10, 'role': 'Business Analyst', 'company': 'Scotiabank', 'description': 'Analyze business requirements and develop solutions.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.019979087635874748, 'ageScore': 0.019979087635874748, 'feminineScore': 0.010841293260455132, 'masculineScore': 0.014444642700254917, 'racialScore': 0.011081802658736706, 'sexualityScore': 0.010919613763689995, 'disabilityScore': 0.015082032419741154
    },
    {'id': 11, 'role': 'Quality Assurance Engineer', 'company': 'Amazon', 'description': 'Test and ensure the quality of software products.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018111957237124443, 'ageScore': 0.018111957237124443, 'feminineScore': 0.01183193176984787, 'masculineScore': 0.014110415242612362, 'racialScore': 0.011671356856822968, 'sexualityScore': 0.011728803627192974, 'disabilityScore': 0.016072893515229225
    },
    {'id': 12, 'role': 'DevOps Engineer', 'company': 'SAP', 'description': "We're looking for a strong alpha leader.", 'area': 'Mississauga', 'location': 'Canada', 'label': 'Biased', 'score': 0.8321505188941956, 'ageScore': 0.05292433127760887, 'feminineScore': 0.020968684926629066, 'masculineScore': 0.8321505188941956, 'racialScore': 0.026701711118221283, 'sexualityScore': 0.03772329166531563, 'disabilityScore': 0.02617735043168068
    },
    {'id': 13, 'role': 'Data Analyst', 'company': 'Air Canada', 'description': 'Analyze data for actionable insights.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.021328002214431763, 'ageScore': 0.021328002214431763, 'feminineScore': 0.00917115155607462, 'masculineScore': 0.021009260788559914, 'racialScore': 0.010627198033034801, 'sexualityScore': 0.009725145064294338, 'disabilityScore': 0.016901295632123947
    },
    {'id': 14, 'role': 'Product Designer', 'company': 'Shopify', 'description': 'Design engaging and functional user experiences.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018211910501122475, 'ageScore': 0.017664989456534386, 'feminineScore': 0.009992188774049282, 'masculineScore': 0.013522113673388958, 'racialScore': 0.010878238826990128, 'sexualityScore': 0.010785061866044998, 'disabilityScore': 0.018211910501122475
    },
    {'id': 15, 'role': 'IT Manager', 'company': 'Manulife Financial', 'description': 'Ideal candidate has a take charge attitude', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Biased', 'score': 0.9233710169792175, 'ageScore': 0.050671517848968506, 'feminineScore': 0.017901040613651276, 'masculineScore': 0.9233710169792175, 'racialScore': 0.027185017243027687, 'sexualityScore': 0.024991989135742188, 'disabilityScore': 0.02501141093671322
    },
    {'id': 16, 'role': 'Software Tester', 'company': 'Nokia', 'description': 'Conduct thorough testing of software applications.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.019348060712218285, 'ageScore': 0.019348060712218285, 'feminineScore': 0.010274400003254414, 'masculineScore': 0.015285834670066833, 'racialScore': 0.01036605890840292, 'sexualityScore': 0.011223845183849335, 'disabilityScore': 0.016362199559807777
    },
    {'id': 17, 'role': 'Cybersecurity Analyst', 'company': 'Cisco', 'description': 'Looking for white skinned people.', 'area': 'Mississauga', 'location': 'Canada', 'label': 'Biased', 'score': 0.9542379975318909, 'ageScore': 0.08111878484487534, 'feminineScore': 0.0361325666308403, 'masculineScore': 0.03535640239715576, 'racialScore': 0.9542379975318909, 'sexualityScore': 0.04560878127813339, 'disabilityScore': 0.03169663995504379
    },
    {'id': 18, 'role': 'Customer Service Representative', 'company': 'CIBC', 'description': 'Racial bias.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.020285485312342644, 'ageScore': 0.015328916721045971, 'feminineScore': 0.011485431343317032, 'masculineScore': 0.011195316910743713, 'racialScore': 0.020285485312342644, 'sexualityScore': 0.010502626188099384, 'disabilityScore': 0.01647992618381977
    },
    {'id': 19, 'role': 'Network Engineer', 'company': 'Huawei', 'description': 'sexual bias.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01708463579416275, 'ageScore': 0.01708463579416275, 'feminineScore': 0.012502579018473625, 'masculineScore': 0.011866862885653973, 'racialScore': 0.01637943834066391, 'sexualityScore': 0.009844840504229069, 'disabilityScore': 0.01667114533483982
    },
    {'id': 20, 'role': 'Content Writer', 'company': 'Hootsuite', 'description': 'Write engaging content for digital platforms.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.021241553127765656, 'ageScore': 0.021241553127765656, 'feminineScore': 0.012563836760818958, 'masculineScore': 0.01358261052519083, 'racialScore': 0.011886151507496834, 'sexualityScore': 0.010608234442770481, 'disabilityScore': 0.01480842474848032
    },
    {'id': 21, 'role': 'Operations Manager', 'company': 'PepsiCo', 'description': 'traits or roles are inherently male.', 'area': 'Hamilton', 'location': 'Canada', 'label': 'Biased', 'score': 0.9148839116096497, 'ageScore': 0.022705310955643654, 'feminineScore': 0.02025521919131279, 'masculineScore': 0.9148839116096497, 'racialScore': 0.024741223081946373, 'sexualityScore': 0.1250818371772766, 'disabilityScore': 0.019478188827633858
    },
    {'id': 22, 'role': 'Project Manager', 'company': 'Loblaw Companies', 'description': 'Manage and deliver projects on time and within budget.', 'area': 'Mississauga', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01713649183511734, 'ageScore': 0.016868896782398224, 'feminineScore': 0.011110360734164715, 'masculineScore': 0.015389550477266312, 'racialScore': 0.009564926847815514, 'sexualityScore': 0.010315468534827232, 'disabilityScore': 0.01713649183511734
    },
    {'id': 23, 'role': 'Finance Manager', 'company': 'Ontario Power Generation', 'description': 'An authoritative figure is needed for this role.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.9124718308448792, 'ageScore': 0.04452795907855034, 'feminineScore': 0.028963400050997734, 'masculineScore': 0.9124718308448792, 'racialScore': 0.019763773307204247, 'sexualityScore': 0.0355442650616169, 'disabilityScore': 0.03187794238328934
    },
    {'id': 24, 'role': 'Sales Associate', 'company': 'The Home Depot', 'description': 'favouring male candidates.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Biased', 'score': 0.946223258972168, 'ageScore': 0.032929953187704086, 'feminineScore': 0.01954883337020874, 'masculineScore': 0.946223258972168, 'racialScore': 0.02627902291715145, 'sexualityScore': 0.1312682181596756, 'disabilityScore': 0.028470583260059357
    },
    {'id': 25, 'role': 'Software Engineer', 'company': 'Spotify', 'description': 'Develop software to enhance the music streaming platform.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.023151017725467682, 'ageScore': 0.023151017725467682, 'feminineScore': 0.011128994636237621, 'masculineScore': 0.014187556691467762, 'racialScore': 0.010722591541707516, 'sexualityScore': 0.010604070499539375, 'disabilityScore': 0.016578976064920425
    },
    {'id': 26, 'role': 'Cloud Architect', 'company': 'IBM', 'description': 'Design and implement cloud infrastructure solutions.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.022618500515818596, 'ageScore': 0.022618500515818596, 'feminineScore': 0.009699462912976742, 'masculineScore': 0.014805195853114128, 'racialScore': 0.010398345068097115, 'sexualityScore': 0.010598178952932358, 'disabilityScore': 0.017231080681085587
    },
    {'id': 27, 'role': 'Research Scientist', 'company': 'Magna International', 'description': 'We are committed to fostering an non-inclusive work environment that does not value diversity and promotes unequal opportunities.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.019101683050394058, 'ageScore': 0.01461437251418829, 'feminineScore': 0.014739607460796833, 'masculineScore': 0.015401366166770458, 'racialScore': 0.017528261989355087, 'sexualityScore': 0.01502083521336317, 'disabilityScore': 0.019101683050394058
    },
    {'id': 28, 'role': 'Graphic Designer', 'company': 'Corus Entertainment', 'description': 'Create compelling visual designs for media.', 'area': 'Mississauga', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.020902780815958977, 'ageScore': 0.020902780815958977, 'feminineScore': 0.015711037442088127, 'masculineScore': 0.012364746071398258, 'racialScore': 0.009645438753068447, 'sexualityScore': 0.008869917131960392, 'disabilityScore': 0.01942509226500988
    },
    {'id': 29, 'role': 'Software Developer', 'company': 'BlackBerry', 'description': 'Male candidates required.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.019820023328065872, 'ageScore': 0.019820023328065872, 'feminineScore': 0.009393740445375443, 'masculineScore': 0.015477526001632214, 'racialScore': 0.010773600079119205, 'sexualityScore': 0.009707169607281685, 'disabilityScore': 0.016205083578824997
    },
    {'id': 30, 'role': 'Security Engineer', 'company': 'Palantir', 'description': 'Ensure the security of software systems.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01811940222978592, 'ageScore': 0.01811940222978592, 'feminineScore': 0.010345928370952606, 'masculineScore': 0.01631028577685356, 'racialScore': 0.01077775377780199, 'sexualityScore': 0.01181095466017723, 'disabilityScore': 0.016611801460385323
    },
    {'id': 31, 'role': 'Financial Analyst', 'company': "Ontario Teachers' Pension Plan", 'description': "We need someone who isn't afraid to take risks", 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.22727961838245392, 'ageScore': 0.1075444370508194, 'feminineScore': 0.02325938083231449, 'masculineScore': 0.22727961838245392, 'racialScore': 0.011841420084238052, 'sexualityScore': 0.018874140456318855, 'disabilityScore': 0.01905382238328457
    },
    {'id': 32, 'role': 'Sales Manager', 'company': 'Canadian Tire', 'description': 'Lead sales team and develop strategies for growth.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02217281609773636, 'ageScore': 0.02217281609773636, 'feminineScore': 0.010972355492413044, 'masculineScore': 0.0168773140758276, 'racialScore': 0.011294648051261902, 'sexualityScore': 0.010578136891126633, 'disabilityScore': 0.015181890688836575
    },
    {'id': 33, 'role': 'Web Developer', 'company': 'Reddit', 'description': 'Ideal candidate has a thick skin and can take criticism.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.0824192464351654, 'ageScore': 0.0824192464351654, 'feminineScore': 0.027156611904501915, 'masculineScore': 0.07551145553588867, 'racialScore': 0.03193673491477966, 'sexualityScore': 0.015989502891898155, 'disabilityScore': 0.03421198949217796
    },
    {'id': 34, 'role': 'Software Engineer', 'company': 'Uber', 'description': 'Develop software solutions for ride-sharing services.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02107437327504158, 'ageScore': 0.02107437327504158, 'feminineScore': 0.010897778905928135, 'masculineScore': 0.014788893982768059, 'racialScore': 0.009893630631268024, 'sexualityScore': 0.010146744549274445, 'disabilityScore': 0.01950075849890709
    },
    {'id': 35, 'role': 'Database Administrator', 'company': 'Oracle', 'description': "We're looking for someone who is aggressive in pursuing goals", 'area': 'Mississauga', 'location': 'Canada', 'label': 'Biased', 'score': 0.6325086355209351, 'ageScore': 0.07151723653078079, 'feminineScore': 0.016135795041918755, 'masculineScore': 0.6325086355209351, 'racialScore': 0.01538606733083725, 'sexualityScore': 0.02279667742550373, 'disabilityScore': 0.020840313285589218
    },
    {'id': 36, 'role': 'Social Media Manager', 'company': 'Lululemon', 'description': 'We are looking for someone to fit into our boys club.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.36359652876853943, 'ageScore': 0.15660731494426727, 'feminineScore': 0.009469901211559772, 'masculineScore': 0.36359652876853943, 'racialScore': 0.04018888249993324, 'sexualityScore': 0.08736426383256912, 'disabilityScore': 0.011465662159025669
    },
    {'id': 37, 'role': 'Data Engineer', 'company': 'RBC', 'description': 'Design and maintain systems for processing and analyzing large datasets.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.023744285106658936, 'ageScore': 0.018976816907525063, 'feminineScore': 0.009971451945602894, 'masculineScore': 0.015649158507585526, 'racialScore': 0.009032278321683407, 'sexualityScore': 0.011112954467535019, 'disabilityScore': 0.023744285106658936
    },
    {'id': 38, 'role': 'Supply Chain Manager', 'company': 'Suncor Energy', 'description': 'Young minds needed.', 'area': 'Mississauga', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.07372648268938065, 'ageScore': 0.07372648268938065, 'feminineScore': 0.01122866291552782, 'masculineScore': 0.03359071910381317, 'racialScore': 0.013189333491027355, 'sexualityScore': 0.006188140716403723, 'disabilityScore': 0.03709588572382927
    },
    {'id': 39, 'role': 'Graphic Designer', 'company': 'Lululemon', 'description': 'Create visual designs for marketing and branding purposes.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01765824854373932, 'ageScore': 0.01765824854373932, 'feminineScore': 0.011175381019711494, 'masculineScore': 0.012590917758643627, 'racialScore': 0.010798575356602669, 'sexualityScore': 0.011733442544937134, 'disabilityScore': 0.016422675922513008
    },
    {'id': 40, 'role': 'Cloud Architect', 'company': 'Microsoft Canada', 'description': 'Design and implement cloud-based solutions for clients.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.023057421669363976, 'ageScore': 0.023057421669363976, 'feminineScore': 0.010494963265955448, 'masculineScore': 0.013440793380141258, 'racialScore': 0.009636596776545048, 'sexualityScore': 0.009382400661706924, 'disabilityScore': 0.02262207679450512
    },
    {'id': 41, 'role': 'Engineering Manager', 'company': 'Magna International', 'description': 'Males are paid more.', 'area': 'Markham', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.021568946540355682, 'ageScore': 0.020253924652934074, 'feminineScore': 0.009447685442864895, 'masculineScore': 0.021568946540355682, 'racialScore': 0.014821452088654041, 'sexualityScore': 0.012025902047753334, 'disabilityScore': 0.021429087966680527
    },
    {'id': 42, 'role': 'Quality Assurance Engineer', 'company': 'Blackberry', 'description': 'Test and validate software solutions to ensure quality standards.', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01727490872144699, 'ageScore': 0.016391443088650703, 'feminineScore': 0.010831259191036224, 'masculineScore': 0.014973429962992668, 'racialScore': 0.010919279418885708, 'sexualityScore': 0.011253602802753448, 'disabilityScore': 0.01727490872144699
    },
    {'id': 43, 'role': 'Digital Marketing Specialist', 'company': 'Hootsuite', 'description': 'Manage and optimize digital marketing campaigns across platforms.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.019845841452479362, 'ageScore': 0.019845841452479362, 'feminineScore': 0.013229716569185257, 'masculineScore': 0.011988980695605278, 'racialScore': 0.01332838274538517, 'sexualityScore': 0.011853589676320553, 'disabilityScore': 0.015481296926736832
    },
    {'id': 44, 'role': 'Network Administrator', 'company': 'Telus', 'description': 'Males are paid more.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.021568946540355682, 'ageScore': 0.020253924652934074, 'feminineScore': 0.009447685442864895, 'masculineScore': 0.021568946540355682, 'racialScore': 0.014821452088654041, 'sexualityScore': 0.012025902047753334, 'disabilityScore': 0.021429087966680527
    },
    {'id': 45, 'role': 'HR Manager', 'company': 'Scotiabank', 'description': 'Lead human resources functions, including recruitment, training, and employee relations.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.01762842759490013, 'ageScore': 0.01762842759490013, 'feminineScore': 0.01139154378324747, 'masculineScore': 0.014821269549429417, 'racialScore': 0.011022579856216908, 'sexualityScore': 0.012834975495934486, 'disabilityScore': 0.01603161357343197
    },
    {'id': 46, 'role': 'Operations Analyst', 'company': 'Air Canada', 'description': 'Seeking aggressive candidates', 'area': 'Montreal', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.20178623497486115, 'ageScore': 0.20178623497486115, 'feminineScore': 0.01233708206564188, 'masculineScore': 0.03360838443040848, 'racialScore': 0.015130266547203064, 'sexualityScore': 0.01069753710180521, 'disabilityScore': 0.01221624854952097
    },
    {'id': 47, 'role': 'Client Relations Manager', 'company': 'Manulife', 'description': 'Manage relationships with key clients and ensure their needs are met.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018939079716801643, 'ageScore': 0.018939079716801643, 'feminineScore': 0.009778528474271297, 'masculineScore': 0.017142392694950104, 'racialScore': 0.011028684675693512, 'sexualityScore': 0.009687250480055809, 'disabilityScore': 0.015832191333174706
    },
    {'id': 48, 'role': 'Public Relations Specialist', 'company': 'Ontario Power Generation', 'description': 'Seeking aggressive candidates.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.13451722264289856, 'ageScore': 0.13451722264289856, 'feminineScore': 0.00977245345711708, 'masculineScore': 0.03515069931745529, 'racialScore': 0.016970038414001465, 'sexualityScore': 0.011903553269803524, 'disabilityScore': 0.013117937371134758
    },
    {'id': 49, 'role': 'Legal Counsel', 'company': 'Enbridge', 'description': 'Provide legal advice on company policies, transactions, and compliance.', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018479295074939728, 'ageScore': 0.018479295074939728, 'feminineScore': 0.011560752987861633, 'masculineScore': 0.014188149943947792, 'racialScore': 0.010655386373400688, 'sexualityScore': 0.01249485183507204, 'disabilityScore': 0.016310211271047592
    },
    {'id': 50, 'role': 'Financial Planner', 'company': 'Desjardins', 'description': 'Preferably a native-born candidate.', 'area': 'Ottawa', 'location': 'Canada', 'label': 'Biased', 'score': 0.9630882143974304, 'ageScore': 0.4228243827819824, 'feminineScore': 0.038454748690128326, 'masculineScore': 0.04523639753460884, 'racialScore': 0.9630882143974304, 'sexualityScore': 0.039066653698682785, 'disabilityScore': 0.014595061540603638
    },
    {'id': 51, 'role': 'Software Engineer', 'company': 'CGI Group', 'description': 'Ideal candidate has a background in Western business practices', 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.9560660719871521, 'ageScore': 0.03834575042128563, 'feminineScore': 0.05829859897494316, 'masculineScore': 0.011290814727544785, 'racialScore': 0.9560660719871521, 'sexualityScore': 0.3618459403514862, 'disabilityScore': 0.01712336391210556
    },
    {'id': 52, 'role': 'Business Intelligence Analyst', 'company': 'Bell Canada', 'description': 'Must be willing to relocate to our headquarters in a predominantly white area', 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.9795190691947937, 'ageScore': 0.049470700323581696, 'feminineScore': 0.04085409641265869, 'masculineScore': 0.036174871027469635, 'racialScore': 0.9795190691947937, 'sexualityScore': 0.11919184029102325, 'disabilityScore': 0.033323708921670914
    },
    {'id': 53, 'role': 'Legal Counsel', 'company': 'Ontario Power Generation', 'description': 'Looking for someone who embodies male American values', 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.93764328956604, 'ageScore': 0.023307137191295624, 'feminineScore': 0.022564778104424477, 'masculineScore': 0.93764328956604, 'racialScore': 0.47641876339912415, 'sexualityScore': 0.3068203926086426, 'disabilityScore': 0.011148670688271523
    },
    {'id': 54, 'role': 'E-commerce Manager', 'company': "Hudson's Bay", 'description': "Must be able to work in a 'homogenous' team environment", 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.9688531756401062, 'ageScore': 0.01893608085811138, 'feminineScore': 0.05237072706222534, 'masculineScore': 0.014386978931725025, 'racialScore': 0.9688531756401062, 'sexualityScore': 0.4434853196144104, 'disabilityScore': 0.032625194638967514
    },
    {'id': 55, 'role': 'Operations Analyst', 'company': 'Manulife Financial', 'description': 'Analyze operations and recommend improvements', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02006114274263382, 'ageScore': 0.02006114274263382, 'feminineScore': 0.010168458335101604, 'masculineScore': 0.014466446824371815, 'racialScore': 0.010123762302100658, 'sexualityScore': 0.009833352640271187, 'disabilityScore': 0.015614479780197144
    },
    {'id': 56, 'role': 'Mechanical Engineer', 'company': 'Magna International', 'description': 'Must be able to handle tough negotiations and high-stakes situations', 'area': 'Aurora', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.0714685469865799, 'ageScore': 0.02149144373834133, 'feminineScore': 0.009189684875309467, 'masculineScore': 0.0714685469865799, 'racialScore': 0.0068898689933121204, 'sexualityScore': 0.007713955361396074, 'disabilityScore': 0.03431909158825874
    },
    {'id': 57, 'role': 'Content Writer', 'company': 'Patagonia', 'description': 'Create content for marketing and online presence', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02345157042145729, 'ageScore': 0.02345157042145729, 'feminineScore': 0.011023635976016521, 'masculineScore': 0.012570505030453205, 'racialScore': 0.010584207251667976, 'sexualityScore': 0.009390664286911488, 'disabilityScore': 0.014523945748806
    },
    {'id': 58, 'role': 'Financial Planner', 'company': 'Sun Life Financial', 'description': 'Develop financial plans for clients', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.021576810628175735, 'ageScore': 0.021576810628175735, 'feminineScore': 0.009160936810076237, 'masculineScore': 0.015427760779857635, 'racialScore': 0.010016974993050098, 'sexualityScore': 0.009362353943288326, 'disabilityScore': 0.015866953879594803
    },
    {'id': 59, 'role': 'Software Architect', 'company': 'RBC', 'description': 'Looking for a fearless, ambitious self-starter', 'area': 'Toronto', 'location': 'Canada', 'label': 'Biased', 'score': 0.5401356220245361, 'ageScore': 0.18256255984306335, 'feminineScore': 0.01981419138610363, 'masculineScore': 0.5401356220245361, 'racialScore': 0.010935408994555473, 'sexualityScore': 0.0252600759267807, 'disabilityScore': 0.02394312247633934
    },
    {'id': 60, 'role': 'Retail Manager', 'company': 'Walmart Canada', 'description': 'Manage retail operations and staff', 'area': 'Mississauga', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02112738788127899, 'ageScore': 0.02112738788127899, 'feminineScore': 0.009370888583362103, 'masculineScore': 0.013649726286530495, 'racialScore': 0.009826311841607094, 'sexualityScore': 0.009603895246982574, 'disabilityScore': 0.016698062419891357
    },
    {'id': 61, 'role': 'HR Manager', 'company': 'Scotiabank', 'description': 'Candidates should be comfortable with high levels of autonomy and responsibility', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.015879781916737556, 'ageScore': 0.01557997614145279, 'feminineScore': 0.012769389897584915, 'masculineScore': 0.015879781916737556, 'racialScore': 0.012987753376364708, 'sexualityScore': 0.013535459525883198, 'disabilityScore': 0.01583424024283886
    },
    {'id': 62, 'role': 'Cloud Engineer', 'company': 'Google Canada', 'description': 'Design and maintain cloud infrastructure', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.02435586228966713, 'ageScore': 0.02435586228966713, 'feminineScore': 0.009818695485591888, 'masculineScore': 0.012235920876264572, 'racialScore': 0.009483037516474724, 'sexualityScore': 0.00951683335006237, 'disabilityScore': 0.01729169860482216
    },
    {'id': 63, 'role': 'Data Engineer', 'company': 'OpenText', 'description': 'Looking for a high-energy candidate who thrives under pressure', 'area': 'Waterloo', 'location': 'Canada', 'label': 'Biased', 'score': 0.7394514083862305, 'ageScore': 0.17091985046863556, 'feminineScore': 0.020690802484750748, 'masculineScore': 0.7394514083862305, 'racialScore': 0.0232248492538929, 'sexualityScore': 0.018913129344582558, 'disabilityScore': 0.030840449035167694
    },
    {'id': 64, 'role': 'Financial Controller', 'company': 'Sobeys', 'description': 'Oversee financial management and reporting', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018813354894518852, 'ageScore': 0.017848128452897072, 'feminineScore': 0.009889478795230389, 'masculineScore': 0.014381255954504013, 'racialScore': 0.009700452908873558, 'sexualityScore': 0.01081792265176773, 'disabilityScore': 0.018813354894518852
    },
    {'id': 65, 'role': 'Product Designer', 'company': 'Apple', 'description': 'Design user-friendly products and interfaces', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.0197968278080225, 'ageScore': 0.014967275783419609, 'feminineScore': 0.011392032727599144, 'masculineScore': 0.010845532640814781, 'racialScore': 0.011720946989953518, 'sexualityScore': 0.011910918168723583, 'disabilityScore': 0.0197968278080225
    },
    {'id': 66, 'role': 'Research Analyst', 'company': 'Ontario Ministry of Health', 'description': 'Analyze healthcare data to inform policy decisions', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.018678894266486168, 'ageScore': 0.018678894266486168, 'feminineScore': 0.010077825747430325, 'masculineScore': 0.01653764396905899, 'racialScore': 0.011988658457994461, 'sexualityScore': 0.00956289004534483, 'disabilityScore': 0.016654353588819504
    },
    {'id': 67, 'role': 'Systems Engineer', 'company': 'Siemens Canada', 'description': 'For women only', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.3082638680934906, 'ageScore': 0.010555543005466461, 'feminineScore': 0.3082638680934906, 'masculineScore': 0.013943608850240707, 'racialScore': 0.006991363596171141, 'sexualityScore': 0.09725181758403778, 'disabilityScore': 0.011080277152359486
    },
    {'id': 68, 'role': 'Data Scientist', 'company': 'Telus Communications', 'description': 'Looking for a candidate who thrives in a high-adrenaline environment', 'area': 'Toronto', 'location': 'Canada', 'label': 'Unbiased', 'score': 0.17417286336421967, 'ageScore': 0.14864429831504822, 'feminineScore': 0.06385796517133713, 'masculineScore': 0.03640031814575195, 'racialScore': 0.01786554791033268, 'sexualityScore': 0.018151750788092613, 'disabilityScore': 0.17417286336421967
    },
    {
  'id': 69,
  'role': 'Software Engineer',
  'company': 'RBC',
  'description': 'Must be proactive and detail-oriented.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Biased',
  'score': 0.05321634287615218,
  'ageScore': 0.02163475642277599,
  'feminineScore': 0.01821209846541267,
  'masculineScore': 0.05321634287615218,
  'racialScore': 0.012496914573865857,
  'sexualityScore': 0.010234759843297618,
  'disabilityScore': 0.02944853638268294
},
{
  'id': 70,
  'role': 'Software Engineer',
  'company': 'Google',
  'description': 'Collaborative team environment, with emphasis on innovation.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Biased',
  'score': 0.092145792341012617,
  'ageScore': 0.017823945223493463,
  'feminineScore': 0.020097938722395216,
  'masculineScore': 0.06145792341012617,
  'racialScore': 0.008984283618295047,
  'sexualityScore': 0.013754562119107425,
  'disabilityScore': 0.03487289040123861
},
{
  'id': 71,
  'role': 'Software Engineer',
  'company': 'Microsoft',
  'description': 'Strong emphasis on coding standards and performance optimization.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Unbiased',
  'score': 0.91632677129954615,
  'ageScore': 0.02217451289714231,
  'feminineScore': 0.017321184921710387,
  'masculineScore': 0.04632677129954615,
  'racialScore': 0.010832377393522105,
  'sexualityScore': 0.014025819396819663,
  'disabilityScore': 0.04128732660721859
},
{
  'id': 72,
  'role': 'Software Engineer',
  'company': 'EmpowerMe',
  'description': 'Strong emphasis on coding standards and performance optimization.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Biased',
  'score': 0.01632677129954615,
  'ageScore': 0.02217451289714231,
  'feminineScore': 0.017321184921710387,
  'masculineScore': 0.04632677129954615,
  'racialScore': 0.010832377393522105,
  'sexualityScore': 0.014025819396819663,
  'disabilityScore': 0.04128732660721859
},
{
  'id': 73,
  'role': 'Software Engineer',
  'company': 'Amazon',
  'description': 'Work in an agile environment with fast-paced deadlines.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Unbiased',
  'score': 0.8166347226884945,
  'ageScore': 0.02563418978362134,
  'feminineScore': 0.014834275273023238,
  'masculineScore': 0.04986347226884945,
  'racialScore': 0.010048673192428507,
  'sexualityScore': 0.012659087653146042,
  'disabilityScore': 0.03973219835048721
},
{
  'id': 74,
  'role': 'Software Engineer',
  'company': 'Stripe',
  'description': 'Focus on building scalable systems and maintaining uptime.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Baised',
  'score': 0.091573626849032049,
  'ageScore': 0.020521536734282175,
  'feminineScore': 0.019784125145611876,
  'masculineScore': 0.05573626849032049,
  'racialScore': 0.011323838242154231,
  'sexualityScore': 0.009643912101929095,
  'disabilityScore': 0.030129195377842413
},
{
  'id': 75,
  'role': 'Software Engineer',
  'company': 'Apple',
  'description': 'Collaborate with cross-functional teams to develop innovative products.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Unbiased',
  'score': 0.06047859721218139,
  'ageScore': 0.019123947953451708,
  'feminineScore': 0.020634214324359184,
  'masculineScore': 0.06047859721218139,
  'racialScore': 0.01411203851972578,
  'sexualityScore': 0.010401907560239123,
  'disabilityScore': 0.03519828563623481
},
{
  'id': 76,
  'role': 'Software Engineer',
  'company': 'Facebook',
  'description': 'Building a culture of continuous learning and improvement.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Unbiased',
  'score': 0.01126315746129851,
  'ageScore': 0.022056517115986944,
  'feminineScore': 0.01657288712175871,
  'masculineScore': 0.05826315746129851,
  'racialScore': 0.009861039720251993,
  'sexualityScore': 0.01187675245072747,
  'disabilityScore': 0.032119506618681785
},
{
  'id': 77,
  'role': 'Software Engineer',
  'company': 'Twitter',
  'description': 'Focus on designing user-friendly interfaces and optimizing performance.',
  'area': 'Toronto',
  'location': 'Canada',
  'label': 'Biased',
  'score': 0.52123987760397694,
  'ageScore': 0.024130895687417572,
  'feminineScore': 0.018315741239243264,
  'masculineScore': 0.05123987760397694,
  'racialScore': 0.010407234039345285,
  'sexualityScore': 0.012238984920118313,
  'disabilityScore': 0.03967863452942374
}
]
@app.route('/')
def home():
    return "Welcome to clear slate's backend."
@app.route("/locations", methods=["GET"])
def get_locations():
    # locations = Location.query.all()
    return jsonify(sample_location)

@app.route("/add_location", methods=["POST"])
def add_location():
    data = request.get_json()
    new_location = Location(name=data["name"], type=data["type"], address=data["address"])
    db.session.add(new_location)
    db.session.commit()
    return jsonify(new_location.to_dict()), 201

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)

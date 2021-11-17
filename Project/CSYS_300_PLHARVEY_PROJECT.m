%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Create an allotaxonomograph %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

name_1 = 'Direct Farm Sales 2007';
name_2 = 'Direct Farm Sales 2012';
name_3 = 'DFS-07-12-rank-div-alpha-5';
daterange = '2007 - 2012';

%% Load Data Manually from .txt unless you're smart with MATLAB...

var1(1).table = DIRSALESFARMS07;
var1(2).table = DIRSALESFARMS12;

indices = [1 2];
for i=1:2
    elements(i).types = var1(indices(i)).table{:,1};
    elements(i).counts = var1(indices(i)).table{:,2};

    elements(i).ranks = tiedrank(elements(i).counts);
    elements(i).totalunique = length(elements(i).types);
end

mixedelements = combine_distributions(elements(1),elements(2));


%% some settings
datetag_str = sprintf(daterange);

settings.system1_name = sprintf(name_1);
settings.system2_name = sprintf(name_2);

settings.typename = 'County';

%%%%%%%%%%%%%%%%%%%%%%
%% general settings %%
%%%%%%%%%%%%%%%%%%%%%%

settings.binwidth = 0.21;
settings.topNshuffling = 25;
settings.topNshift = 40;
settings.topNdeltasum = 'all';

settings.max_plot_string_length = 15;
settings.max_shift_string_length = 25;

settings.imageformat.open = 'no';

settings.plotkind = 'rank';

settings.instrument = 'rank divergence';

%% move the shift (adds to 0.60)
settings.xoffset = +0.00;

%% alphavals = [(0:18)/12, 2, 3, 5, 10, Inf]';

settings.alpha = 5;

tag = sprintf(name_3);

figallotaxonometer9000(mixedelements, tag, settings);
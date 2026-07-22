import re

# WP2
wp2_path = "/home/user0/git/working_papers/wp2_surplus_capacity/ssrn-6211658_Revised.tex"
with open(wp2_path, "r") as f:
    wp2_content = f.read()

scope_pattern = r'\\section\*\{Scope, Purpose, and Limitations\}.*?The limitations identified here do not weaken the argument; they define its boundaries\.\s*\\newpage\s*'
wp2_content = re.sub(scope_pattern, '', wp2_content, flags=re.DOTALL)

with open(wp2_path, "w") as f:
    f.write(wp2_content)

# WP3
wp3_path = "/home/user0/git/working_papers/wp3_los_angeles_pipeline/ssrn-6579600_Revised.tex"
with open(wp3_path, "r") as f:
    wp3_content = f.read()

# Trim necessity
wp3_nec_old = r"""Los Angeles experiences a three-dimensional structural failure involving housing, public health, and fiscal policy. Despite twenty-four billion dollars in expenditure since 2019 forty-six thousand unsheltered individuals remain on the street. Mortality among the unhoused has accelerated to create a thirty-year life expectancy gap. Current systems fail because they violate causal necessity by deploying housing before the physiological prerequisites for maintaining tenure emerge. The United States lacks the foundational layer that allowed Finland to solve chronic homelessness by providing these prerequisites through a unified national welfare infrastructure. The Material Dignity Infrastructure engineers a substitute for this missing infrastructure introducing a Metabolic Stabilization layer as Phase Zero that restores biological prerequisites before any permanent unit offer occurs. The Material Dignity Infrastructure proposes a falsifiable and industrially specified pipeline extending from street engagement through permanent residential stabilization because an alternative framework built on this causal foundation remains required."""
wp3_nec_new = """Los Angeles experiences a three-dimensional structural failure involving housing, public health, and fiscal policy. Despite twenty-four billion dollars in expenditure since 2019, current systems fail because they deploy housing before the physiological prerequisites for maintaining tenure emerge. The United States lacks the foundational layer that allowed Finland to solve chronic homelessness. The Material Dignity Infrastructure engineers a substitute for this missing infrastructure, introducing the Ground Floor Intake Airlock to restore biological prerequisites before any permanent unit offer occurs. This paper specifies the falsifiable pipeline from street engagement through permanent residential stabilization."""
wp3_content = wp3_content.replace(wp3_nec_old, wp3_nec_new)

# Remove Word Count
wp3_content = re.sub(r'\\noindent\\textbf\{Word Count:\}\s*\d+,\d+\s*', '', wp3_content)

# Add TOC
toc_str = r"""
% ── TABLE OF CONTENTS ────
\newpage
\begingroup
\setstretch{1.05}
\setlength{\cftbeforesecskip}{2pt}
\setlength{\cftbeforesubsecskip}{-2pt}
\tableofcontents
\endgroup

% ── BODY ────"""
wp3_content = wp3_content.replace('% ═════════════\n\\clearpage\n\\section{The Los Angeles Inflection Point}', toc_str + '\n\n% ═════════════\n\\clearpage\n\\section{The Los Angeles Inflection Point}')

with open(wp3_path, "w") as f:
    f.write(wp3_content)

# WP4
wp4_path = "/home/user0/git/working_papers/wp4_human_layer/ssrn-6881539_Revised.tex"
with open(wp4_path, "r") as f:
    wp4_content = f.read()

wp4_nec_old = r"""The homelessness policy literature has produced two decades of Housing First evidence demonstrating that permanent housing with wraparound services outperforms treatment-first models. What the literature has not produced is a formal theoretical account of what the relational environment within Housing First infrastructure must contain in order to produce the outcomes that Housing First promises. The result is a gap between architectural intention and human outcome that institutional service systems fill by default with transactional case management behavioral compliance monitoring and the objectification of residents as service recipients minimizing their status as persons under reconstruction. This paper argues that this gap is not a service delivery problem. It is a theoretical problem because the field lacks a named formally defined concept for the relational layer that material housing must contain. Without a concept the layer cannot be designed. Without design it cannot be replicated. Without replication Housing First produces the forty-percent retention rates observed in the American system falling short of the eighty to ninety percent rates observed in the Finnish system. The funding differential between the Finnish and American systems is real and documented and this paper does not contest it. What it contests is the assumption that funding alone explains the retention gap since adequately funded American programs functioning in high-cost urban markets routinely achieve retention well below the Finnish floor and since the Finnish housing advisor role which this paper identifies as the structural analogue of the Pod Steward is a design specification that any sufficiently funded system can replicate regardless of its national policy context. Relational Dignity Infrastructure names the layer defines its production conditions and maps its implementation within the MDI tower architecture as a replicable measurable infrastructure component."""
wp4_nec_new = """The homelessness policy literature has produced two decades of Housing First evidence demonstrating that permanent housing with wraparound services outperforms treatment-first models. What the literature lacks is a formally defined concept for the relational layer that material housing must contain. Without this concept, institutional service systems default to transactional case management and behavioral compliance monitoring, minimizing residents' status as persons under reconstruction. This paper defines Relational Dignity Infrastructure (RDI) as the structural solution to this gap, mapping its implementation within the MDI tower architecture as a replicable, measurable component capable of achieving the eighty to ninety percent retention rates observed in the Finnish system."""
wp4_content = wp4_content.replace(wp4_nec_old, wp4_nec_new)

with open(wp4_path, "w") as f:
    f.write(wp4_content)

print("Standardization applied.")

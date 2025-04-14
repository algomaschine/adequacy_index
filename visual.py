import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import json
import os

# Update emojis at the top of the file
QUADRANT_EMOJIS = {
    'blue': '🔍',    # Magnifying glass for careful analysis/caution
    'red': '⛔',     # No entry sign for danger/stop
    'green': '✅',   # Check mark for positive/growth
    'yellow': '⚠'   # Warning sign for risk/caution
}

# Configuration JSON
CONFIG = {
    "domains": {
        "HR Processes": {
            "phrases": {
                "blue": [
                    "\"We should verify references thoroughly\"",
                    "\"Start with a probation period\"",
                    "\"Need more diversity analysis\"",
                    "\"Double-check compliance\"",
                    "\"Consider internal candidates first\"",
                    "\"Verify skill certifications\"",
                    "\"Implement phased onboarding\"",
                    "\"Conduct thorough skills assessment\"",
                    "\"Review team dynamics impact\"",
                    "\"Conduct cultural alignment assessments\"",
                    "\"Implement blind resume screening\"",
                    "\"Establish whistleblower protection\""
                ],
                "red": [
                    "\"Just hire anyone quickly\"",
                    "\"Ignore cultural fit\"",
                    "\"Fire without documentation\"",
                    "\"Skip background checks\"",
                    "\"Panic hiring decisions\"",
                    "\"Cancel all interviews\"",
                    "\"Freeze hiring indefinitely\"",
                    "\"Eliminate all HR protocols\"",
                    "\"Hire without job description\"",
                    "\"Cancel all team meetings\"",
                    "\"Disable employee feedback channels\"",
                    "\"Cancel all team-building activities\""
                ],
                "green": [
                    "\"Strategic talent development\"",
                    "\"Succession planning\"",
                    "\"Employee growth programs\"",
                    "\"Retention strategy\"",
                    "\"Leadership pipeline\"",
                    "\"Competency framework\"",
                    "\"Performance analytics\"",
                    "\"Implement mentorship networks\"",
                    "\"Develop skills matrix\"",
                    "\"Develop internal mobility programs\"",
                    "\"Create leadership competency models\"",
                    "\"Create executive coaching programs\""
                ],
                "yellow": [
                    "\"Hire 50 people in one week\"",
                    "\"No need for interviews\"",
                    "\"Ignore salary benchmarks\"",
                    "\"Promote without criteria\"",
                    "\"Eliminate all training\"",
                    "\"Automate all hiring\"",
                    "\"Copy competitor org structure\"",
                    "\"Offer unrealistic perks\"",
                    "\"Guarantee promotions\"",
                    "\"Offer signing bonuses indiscriminately\"",
                    "\"Eliminate performance metrics\"",
                    "\"Implement AI-based layoff decisions\""
                ]
            },
            "actions": {
                "blue": [
                    "Implement structured interviews",
                    "Conduct engagement surveys",
                    "Develop mentorship programs",
                    "Create redundancy plans",
                    "Establish clear policies",
                    "Run skills gap analysis",
                    "Implement peer reviews",
                    "Develop cross-training programs",
                    "Establish feedback loops",
                    "Develop succession contingency plans",
                    "Implement AI-driven candidate matching",
                    "Develop psychometric testing"
                ],
                "red": [
                    "Mass layoffs without planning",
                    "Skip performance reviews",
                    "Ignore legal compliance",
                    "Freeze all hiring",
                    "Eliminate benefits abruptly",
                    "Delete candidate pipeline",
                    "Cancel L&D budget",
                    "Remove HR documentation",
                    "Disable career portals",
                    "Delete employee performance records",
                    "Cancel all training budgets",
                    "Eliminate employee resource groups"
                ],
                "green": [
                    "Invest in L&D programs",
                    "Create career paths",
                    "Build employer branding",
                    "Optimize onboarding",
                    "Develop metrics dashboards",
                    "Implement succession planning",
                    "Launch leadership academy",
                    "Establish recognition programs",
                    "Create talent marketplace",
                    "Launch internal gig marketplace",
                    "Implement skills-based promotions",
                    "Implement skills-based compensation"
                ],
                "yellow": [
                    "Hire friends/family",
                    "Copy competitor policies",
                    "Promise unrealistic promotions",
                    "Ignore workplace complaints",
                    "Eliminate HR department",
                    "Double hiring targets",
                    "Automate performance reviews",
                    "Offer stock options indiscriminately",
                    "Guarantee annual bonuses",
                    "Automate employee evaluations",
                    "Guarantee remote work permanently",
                    "Automate promotion decisions"
                ]
            },
            "feelings": {
                "blue": [
                    "Mindful vigilance",
                    "Analytical clarity",
                    "Protective wisdom",
                    "Measured confidence",
                    "Strategic patience",
                    "Calm assessment",
                    "Thoughtful consideration",
                    "Balanced judgment",
                    "Careful optimism",
                    "Professional focus",
                    "Ethical awareness",
                    "Controlled progress"
                ],
                "red": [
                    "Decision paralysis",
                    "Overwhelming dread",
                    "System overload",
                    "Complete shutdown",
                    "Trust collapse",
                    "Defensive panic",
                    "Resource anxiety",
                    "Control loss",
                    "Team fragmentation",
                    "Process chaos",
                    "Morale crash",
                    "Structural failure"
                ],
                "green": [
                    "Growth momentum",
                    "Strategic flow",
                    "Team synergy",
                    "Innovation spark",
                    "Leadership clarity",
                    "Development drive",
                    "Success alignment",
                    "Cultural harmony",
                    "Talent flourishing",
                    "Vision realization",
                    "Achievement high",
                    "Excellence pride"
                ],
                "yellow": [
                    "Reckless euphoria",
                    "Control illusion",
                    "Risk blindness",
                    "Impulsive rush",
                    "Power intoxication",
                    "Reality distortion",
                    "FOMO pressure",
                    "Overconfidence trap",
                    "Decision mania",
                    "Process addiction",
                    "Change obsession",
                    "System overreach"
                ]
            }
        },
        "Relationship Processes": {
            "phrases": {
                "blue": [
                    "\"Let's discuss boundaries\"",
                    "\"Need time to reflect\"",
                    "\"Consider counseling\"",
                    "\"Communicate needs clearly\"",
                    "\"Balance independence\"",
                    "\"Schedule check-in times\"",
                    "\"Establish mutual goals\"",
                    "\"Respect personal space\"",
                    "\"Clarify expectations\"",
                    "\"Establish digital detox periods\"",
                    "\"Create relationship checklists\"",
                    "\"Establish digital communication guidelines\""
                ],
                "red": [
                    "\"Never trust again\"",
                    "\"Avoid all conflict\"",
                    "\"Isolate completely\"",
                    "\"Assume worst intentions\"",
                    "\"End relationship now\"",
                    "\"Ghost partner\"",
                    "\"Burn bridges\"",
                    "\"Delete contact information\"",
                    "\"Publicly shame partner\"",
                    "\"Delete shared photos/videos\"",
                    "\"Block mutual friends\"",
                    "\"Purge shared memories\""
                ],
                "green": [
                    "\"Plan quality time\"",
                    "\"Shared goal setting\"",
                    "\"Regular check-ins\"",
                    "\"Mutual support\"",
                    "\"Healthy compromise\"",
                    "\"Celebrate milestones\"",
                    "\"Practice gratitude\"",
                    "\"Maintain individual friendships\"",
                    "\"Establish relationship rituals\"",
                    "\"Plan surprise appreciation gestures\"",
                    "\"Establish conflict time-outs\"",
                    "\"Create legacy planning\""
                ],
                "yellow": [
                    "\"Move in immediately\"",
                    "\"Ignore red flags\"",
                    "\"Merge finances completely\"",
                    "\"Sacrifice all boundaries\"",
                    "\"Depend entirely\"",
                    "\"Quit job for partner\"",
                    "\"Propose impulsively\"",
                    "\"Co-sign large loans\"",
                    "\"Share all digital accounts\"",
                    "\"Move pets in together hastily\"",
                    "\"Combine social media accounts\"",
                    "\"Combine financial accounts immediately\""
                ]
            },
            "actions": {
                "blue": [
                    "Schedule regular talks",
                    "Maintain personal space",
                    "Set mutual boundaries",
                    "Practice active listening",
                    "Seek third-party help",
                    "Create shared calendar",
                    "Establish conflict protocol",
                    "Plan individual time",
                    "Document agreements",
                    "Create relationship vision board",
                    "Implement weekly appreciation rituals",
                    "Implement relationship health metrics"
                ],
                "red": [
                    "Ghost partner",
                    "Snoop devices",
                    "Make ultimatums",
                    "Withdraw emotionally",
                    "Sabotage connections",
                    "Block on social media",
                    "Destroy mementos",
                    "Change locks unilaterally",
                    "Spread private information",
                    "Destroy shared possessions",
                    "Change relationship status publicly",
                    "Delete shared cloud storage"
                ],
                "green": [
                    "Create shared calendar",
                    "Plan future together",
                    "Develop trust rituals",
                    "Celebrate milestones",
                    "Maintain individual hobbies",
                    "Schedule retreats",
                    "Practice forgiveness",
                    "Establish joint savings",
                    "Create relationship vision board",
                    "Develop shared bucket list",
                    "Establish annual relationship reviews",
                    "Develop couple's mission statement"
                ],
                "yellow": [
                    "Propose impulsively",
                    "Share passwords immediately",
                    "Quit job for partner",
                    "Ignore friends/family",
                    "Make major purchases",
                    "Relocate hastily",
                    "Co-sign loans blindly",
                    "Tattoo partner's name",
                    "Abandon previous commitments",
                    "Purchase matching tattoos",
                    "Cosign mortgage immediately",
                    "Purchase joint life insurance"
                ]
            },
            "feelings": {
                "blue": [
                    "Mindful presence",
                    "Emotional balance",
                    "Secure boundaries",
                    "Thoughtful care",
                    "Patient understanding",
                    "Clear communication",
                    "Mutual respect",
                    "Calm reflection",
                    "Gentle curiosity",
                    "Stable connection",
                    "Trust building",
                    "Conscious growth"
                ],
                "red": [
                    "Emotional shutdown",
                    "Trust collapse",
                    "Abandonment fear",
                    "Defensive walls",
                    "Relationship anxiety",
                    "Connection loss",
                    "Betrayal trauma",
                    "Emotional flooding",
                    "Communication freeze",
                    "Attachment panic",
                    "Identity crisis",
                    "Social isolation"
                ],
                "green": [
                    "Deep connection",
                    "Mutual flourishing",
                    "Secure attachment",
                    "Emotional intimacy",
                    "Shared joy",
                    "Growth synergy",
                    "Trust abundance",
                    "Love expansion",
                    "Relationship flow",
                    "Future excitement",
                    "Partnership pride",
                    "Harmonious bond"
                ],
                "yellow": [
                    "Relationship addiction",
                    "Boundary collapse",
                    "Obsessive attachment",
                    "Identity fusion",
                    "Emotional flooding",
                    "Dependency spiral",
                    "Control mania",
                    "Reality distortion",
                    "Commitment rush",
                    "Trust blindness",
                    "Passion overdrive",
                    "Merger mania"
                ]
            }
        },
        "Business Negotiations": {
            "phrases": {
                "blue": [
                    "\"Verify their BATNA\"",
                    "\"Need legal review\"",
                    "\"Start with small asks\"",
                    "\"Plan walk-away point\"",
                    "\"Consider long-term value\"",
                    "\"Clarify decision makers\"",
                    "\"Verify financials\"",
                    "\"Analyze market benchmarks\"",
                    "\"Confirm authority levels\"",
                    "\"Conduct mock negotiations\"",
                    "\"Verify counterpart's authority\"",
                    "\"Verify counterpart's BATNA validation\""
                ],
                "red": [
                    "\"Accept any terms\"",
                    "\"Reveal budget first\"",
                    "\"Avoid confrontation\"",
                    "\"Panic concessions\"",
                    "\"Take first offer\"",
                    "\"Disclose weaknesses\"",
                    "\"Cancel negotiation\"",
                    "\"Reveal internal conflicts\"",
                    "\"Share confidential data\"",
                    "\"Reveal internal cost structures\"",
                    "\"Adopt passive-aggressive tactics\"",
                    "\"Reveal internal salary data\""
                ],
                "green": [
                    "\"Create win-win scenarios\"",
                    "\"Anchor effectively\"",
                    "\"Leverage strengths\"",
                    "\"Build relationships\"",
                    "\"Strategic concessions\"",
                    "\"Identify mutual gains\"",
                    "\"Establish trust\"",
                    "\"Develop package deals\"",
                    "\"Use objective criteria\"",
                    "\"Leverage third-party benchmarks\"",
                    "\"Develop concession hierarchies\"",
                    "\"Develop negotiation playbooks\""
                ],
                "yellow": [
                    "\"Bluff about alternatives\"",
                    "\"Threaten to walk out\"",
                    "\"Demand impossible terms\"",
                    "\"Hide information\"",
                    "\"Personal attacks\"",
                    "\"Fake deadlines\"",
                    "\"Inflate numbers\"",
                    "\"Promise undeliverables\"",
                    "\"Reveal competitor offers\"",
                    "\"Fabricate competitor offers\"",
                    "\"Use emotional blackmail\"",
                    "\"Bluff regulatory connections\""
                ]
            },
            "actions": {
                "blue": [
                    "Prepare negotiation matrix",
                    "Research counterpart",
                    "Set clear objectives",
                    "Use silence strategically",
                    "Document agreements",
                    "Verify claims",
                    "Schedule follow-ups",
                    "Conduct scenario planning",
                    "Establish verification process",
                    "Implement negotiation playbooks",
                    "Conduct BATNA simulations",
                    "Implement cultural alignment checks"
                ],
                "red": [
                    "Reveal deadlines",
                    "Accept verbal promises",
                    "Skip due diligence",
                    "Make unilateral offers",
                    "Avoid eye contact",
                    "Accept unfavorable terms",
                    "Burn documents",
                    "Disclose bottom line",
                    "Cancel preparation meetings",
                    "Share internal meeting minutes",
                    "Accept unfavorable payment terms",
                    "Accept unfavorable arbitration clauses"
                ],
                "green": [
                    "Frame proposals effectively",
                    "Use reciprocity",
                    "Leverage objective criteria",
                    "Build rapport",
                    "Close with clear terms",
                    "Identify ZOPA",
                    "Use bracketing",
                    "Employ good cop/bad cop",
                    "Leverage third-party endorsements",
                    "Develop value-creation matrix",
                    "Implement post-negotiation reviews",
                    "Create value mapping frameworks"
                ],
                "yellow": [
                    "Make take-it-or-leave-it",
                    "Use false deadlines",
                    "Exaggerate alternatives",
                    "Burn bridges",
                    "Reveal confidential info",
                    "Threaten legal action",
                    "Fake competition",
                    "Promise unauthorized terms",
                    "Bluff about walk-away power",
                    "Threaten regulatory complaints",
                    "Promise exclusive partnerships",
                    "Promise board seat access"
                ]
            },
            "feelings": {
                "blue": [
                    "Strategic focus",
                    "Analytical clarity",
                    "Controlled patience",
                    "Data confidence",
                    "Risk awareness",
                    "Measured trust",
                    "Professional detachment",
                    "Tactical readiness",
                    "Calm assessment",
                    "Objective judgment",
                    "Strategic composure",
                    "Prepared mindset"
                ],
                "red": [
                    "Negotiation anxiety",
                    "Power loss",
                    "Trust breakdown",
                    "Decision paralysis",
                    "Value erosion",
                    "Position weakness",
                    "Control loss",
                    "Defensive panic",
                    "Resource drain",
                    "Strategy collapse",
                    "Confidence crash",
                    "Deal anxiety"
                ],
                "green": [
                    "Value creation",
                    "Strategic flow",
                    "Deal momentum",
                    "Partnership synergy",
                    "Negotiation mastery",
                    "Trust building",
                    "Win-win confidence",
                    "Growth alignment",
                    "Deal enthusiasm",
                    "Strategic clarity",
                    "Value optimization",
                    "Success momentum"
                ],
                "yellow": [
                    "Power intoxication",
                    "Control illusion",
                    "Deal obsession",
                    "Risk blindness",
                    "Victory addiction",
                    "Reality distortion",
                    "Dominance rush",
                    "Overconfidence trap",
                    "Position mania",
                    "Trust recklessness",
                    "Strategy gambling",
                    "Power euphoria"
                ]
            }
        },
        "Financial Trading": {
            "phrases": {
                "blue": [
                    "\"Maintain stop-loss\"",
                    "\"Diversify portfolio\"",
                    "\"Verify fundamentals\"",
                    "\"Stick to strategy\"",
                    "\"Preserve capital\"",
                    "\"Rebalance quarterly\"",
                    "\"Hedge positions\"",
                    "\"Review economic indicators\"",
                    "\"Maintain liquidity buffer\"",
                    "\"Implement volatility alerts\"",
                    "\"Review black swan scenarios\"",
                    "\"Implement position size calculators\""
                ],
                "red": [
                    "\"Sell everything now\"",
                    "\"Avoid all risk\"",
                    "\"Market will crash\"",
                    "\"Lock in losses\"",
                    "\"Panic liquidate\"",
                    "\"Ignore opportunities\"",
                    "\"Freeze accounts\"",
                    "\"Withdraw all funds\"",
                    "\"Cancel limit orders\"",
                    "\"Convert to stablecoins exclusively\"",
                    "\"Delete trading algorithms\"",
                    "\"Convert to cash equivalents\""
                ],
                "green": [
                    "\"Scale proven strategies\"",
                    "\"Reinvest profits\"",
                    "\"Optimize tax efficiency\"",
                    "\"Dollar-cost average\"",
                    "\"Long-term holds\"",
                    "\"Sector rotation\"",
                    "\"Value investing\"",
                    "\"Compound dividends\"",
                    "\"Automate contributions\"",
                    "\"Analyze sector correlations\"",
                    "\"Implement tax optimization strategies\"",
                    "\"Analyze factor exposures\""
                ],
                "yellow": [
                    "\"Leverage 10:1\"",
                    "\"Follow meme stocks\"",
                    "\"All-in on crypto\"",
                    "\"Ignore fundamentals\"",
                    "\"Chase pumps\"",
                    "\"Day trade savings\"",
                    "\"Margin call risk\"",
                    "\"Short without hedge\"",
                    "\"Trade illiquid assets\"",
                    "\"Trade during earnings announcements\"",
                    "\"Use high-frequency trading bots\"",
                    "\"Trade penny stocks aggressively\""
                ]
            },
            "actions": {
                "blue": [
                    "Set risk parameters",
                    "Maintain cash reserve",
                    "Review fundamentals",
                    "Diversify assets",
                    "Use trailing stops",
                    "Analyze macro trends",
                    "Document trades",
                    "Implement position sizing",
                    "Schedule portfolio reviews",
                    "Implement scenario analysis tools",
                    "Develop liquidity contingency plans",
                    "Implement volatility-adjusted allocations"
                ],
                "red": [
                    "Sell at market open",
                    "Close all positions",
                    "Withdraw funds",
                    "Ignore technicals",
                    "Cancel limit orders",
                    "Freeze activity",
                    "Delete trading apps",
                    "Convert to cash only",
                    "Avoid market news",
                    "Sell dividend-paying stocks",
                    "Cancel stop-loss orders",
                    "Sell dividend aristocrats"
                ],
                "green": [
                    "Reinvest dividends",
                    "Automate investments",
                    "Research sectors",
                    "Tax-loss harvest",
                    "DCA into positions",
                    "Review holdings",
                    "Update will/trust",
                    "Optimize asset allocation",
                    "Analyze cash flow",
                    "Optimize portfolio beta",
                    "Implement risk parity strategies",
                    "Optimize portfolio convexity"
                ],
                "yellow": [
                    "Max out margin",
                    "Follow influencers",
                    "Trade exotic options",
                    "Ignore stop-losses",
                    "Liquidate assets",
                    "Borrow to invest",
                    "Day trade full-time",
                    "Chase overnight gaps",
                    "Overconcentrate positions",
                    "Trade exotic derivatives",
                    "Short volatility ETFs",
                    "Trade without hedging"
                ]
            },
            "feelings": {
                "blue": [
                    "Risk awareness",
                    "Analytical focus",
                    "Strategic patience",
                    "Data confidence",
                    "Market respect",
                    "Position control",
                    "Systematic calm",
                    "Technical clarity",
                    "Capital preservation",
                    "Trend awareness",
                    "Risk management",
                    "Strategic composure"
                ],
                "red": [
                    "Market panic",
                    "Loss paralysis",
                    "Portfolio anxiety",
                    "Value erosion",
                    "Position fear",
                    "Trading freeze",
                    "Capital flight",
                    "Market trauma",
                    "Strategy collapse",
                    "Risk spiral",
                    "Confidence crash",
                    "Account dread"
                ],
                "green": [
                    "Trading flow",
                    "Growth momentum",
                    "Position confidence",
                    "Market mastery",
                    "Strategy synergy",
                    "Portfolio harmony",
                    "Profit satisfaction",
                    "Investment clarity",
                    "Trend alignment",
                    "Success momentum",
                    "Value creation",
                    "Trading excellence"
                ],
                "yellow": [
                    "Trading addiction",
                    "Risk euphoria",
                    "Position mania",
                    "Market obsession",
                    "FOMO overdrive",
                    "Leverage intoxication",
                    "Profit blindness",
                    "Strategy gambling",
                    "Trading trance",
                    "Market invincibility",
                    "Position greed",
                    "Account overconfidence"
                ]
            }
        }
    }
}
def render_diagrams(domain, content_type, ax, emoji_font):
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_facecolor('#FFFFFF')
    
    # Remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # Axis labels
    ax.text(1.05, 0, 'Greed', ha='left', va='center', fontsize=10, color='#444444')
    ax.text(-1.05, 0, 'Fear', ha='right', va='center', fontsize=10, color='#444444')
    ax.text(0, 1.05, 'Rational', ha='center', va='bottom', fontsize=10, color='#444444')
    ax.text(0, -1.05, 'Irrational', ha='center', va='top', fontsize=10, color='#444444')
    
    # Quadrant colors
    quadrant_colors = {
        'red': '#FF9999',
        'blue': '#9999FF',
        'green': '#99FF99',
        'yellow': '#FFFF99'
    }
    
    # Draw quadrant backgrounds
    for q in [((-1, 0), 1, 1, 'blue'), 
              ((-1, -1), 1, 1, 'red'),
              ((0, 0), 1, 1, 'green'),
              ((0, -1), 1, 1, 'yellow')]:
        ax.add_patch(patches.Rectangle(q[0], q[1], q[2], 
                                     facecolor=quadrant_colors[q[3]], alpha=0.3))
    
    quadrant_data = [
        {'pos': (-0.5, 0.5), 'zone': 'Cautious', 'icon': '🔍', 'color': '#0000AA', 'color_name': 'blue'},
        {'pos': (-0.5, -0.5), 'zone': 'Panic', 'icon': '⛔', 'color': '#AA0000', 'color_name': 'red'},
        {'pos': (0.5, 0.5), 'zone': 'Ambition', 'icon': '✅', 'color': '#00AA00', 'color_name': 'green'},
        {'pos': (0.5, -0.5), 'zone': 'Adventure', 'icon': '⚠', 'color': '#AAAA00', 'color_name': 'yellow'}
    ]
    
    # Create legend patches
    legend_patches = []
    legend_labels = []
    
    for qd in quadrant_data:
        patch = patches.Patch(facecolor=quadrant_colors[qd['color_name']], 
                            alpha=0.3, 
                            label=f"{qd['icon']} {qd['zone']}")
        legend_patches.append(patch)
        legend_labels.append(f"{qd['icon']} {qd['zone']}")
    
    # Add legend outside the plot
    legend = ax.legend(legend_patches, legend_labels,
                      loc='center left',
                      bbox_to_anchor=(1.25, 0.5),
                      fontsize=10,
                      prop=emoji_font,
                      title='Quadrants',
                      title_fontsize=12,
                      frameon=True,
                      facecolor='white',
                      edgecolor='#CCCCCC')
    
    # Add content
    for qd in quadrant_data:
        content = CONFIG['domains'][domain][content_type][qd['color_name']]
        y_start = qd['pos'][1] + 0.45  # Starting position
        line_height = 0.075  # Same for all content types
        fontsize = 5  # Same base size for all
        
        for i, text in enumerate(content[:12]):
            y_pos = y_start - (i * line_height)
            ax.text(qd['pos'][0], y_pos, text,
                    fontsize=fontsize, 
                    ha='center', 
                    va='top', 
                    color='#444444',
                    linespacing=1.08)
    
    # Add adequacy scale
    scale_left = 1.25  # Moved right to align with legend
    scale_bottom = 0.15
    scale_width = 0.3
    scale_height = 0.04
    
    ax.add_patch(patches.Rectangle((scale_left, scale_bottom), scale_width, scale_height,
                                 transform=ax.transAxes,
                                 facecolor='white',
                                 edgecolor='#CCCCCC',
                                 clip_on=False))
    
    # Add title for adequacy scale
    ax.text(scale_left + scale_width/2, scale_bottom + scale_height + 0.02,
            'Adequacy Index',
            transform=ax.transAxes,
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold')
    
    # Smooth color gradient
    def interpolate_color(color1, color2, t):
        return tuple(max(0, min(1, c1 * (1-t) + c2 * t)) for c1, c2 in zip(color1, color2))
    
    # Define colors for gradient
    red = (1.0, 0.0, 0.0)      # Panic
    blue = (0.0, 0.0, 1.0)     # Cautious
    yellow = (1.0, 1.0, 0.0)   # Adventure
    green = (0.0, 1.0, 0.0)    # Ambition
    
    # Create smooth gradient
    for i in range(101):
        x_pos = scale_left + (i/100) * scale_width
        t = i / 100
        
        if t <= 0.2:  # 0-20%: Red to Blue
            color = interpolate_color(red, blue, t/0.2)
        elif t <= 0.5:  # 20-50%: Blue to Yellow
            t2 = (t - 0.2) / 0.3
            color = interpolate_color(blue, yellow, t2)
        elif t <= 0.8:  # 50-80%: Yellow to Green
            t2 = (t - 0.5) / 0.3
            color = interpolate_color(yellow, green, t2)
        else:  # 80-100%: Stay Green
            color = green
        
        ax.plot([x_pos, x_pos],
                [scale_bottom, scale_bottom + scale_height],
                transform=ax.transAxes,
                color=color,
                lw=1,
                clip_on=False)
    
    # Number labels
    for i in range(0, 11, 2):
        x_pos = scale_left + (i/10) * scale_width
        ax.text(x_pos, scale_bottom - 0.02, str(i),
                transform=ax.transAxes,
                ha='center', va='top', fontsize=8)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{domain} - {content_type.capitalize()}", 
                fontsize=12, fontweight='bold', pad=12)

# Main rendering function
def generate_all_diagrams():
    # Font setup with multiple fallbacks
    plt.rcParams['font.family'] = ['Segoe UI Emoji', 'Segoe UI Symbol', 'Segoe UI Historic', 'DejaVu Sans']
    
    # Try to find and use Segoe UI Emoji font
    font_path = 'C:/Windows/Fonts/seguiemj.ttf'  # Segoe UI Emoji font path
    if os.path.exists(font_path):
        font_manager.fontManager.addfont(font_path)
        emoji_font = font_manager.FontProperties(fname=font_path)
    else:
        # Fallback to system emoji fonts
        emoji_font = font_manager.FontProperties(family='Segoe UI Emoji')
    
    for domain in CONFIG['domains']:
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 21), dpi=300)  # Increased height for 3 plots
        fig.patch.set_facecolor('#FFFFFF')
        
        render_diagrams(domain, 'phrases', ax1, emoji_font)
        render_diagrams(domain, 'actions', ax2, emoji_font)
        render_diagrams(domain, 'feelings', ax3, emoji_font)
        
        plt.tight_layout(pad=2.0)
        filename = f"{domain.lower().replace(' ', '_')}_adequacy_index.png"
        plt.savefig(filename, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Generated: {filename}")

# Run the generator
if __name__ == "__main__":
    generate_all_diagrams()
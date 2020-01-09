const coloring_aa = d3.scaleOrdinal(d3.schemeCategory20);
function coloring(name, value){
  if(name === 'Codon Usage'){
    return 'white'
  }
  if(name === 'A'){
    return 'rgb(255, 143, 145)'
  }
  if(name === 'T'){
    return 'rgb(86, 255, 95)'
  }
  if(name === 'C'){
    return 'rgb(144, 204, 255)'
  }
  if(name === 'G'){
    return 'rgb(248, 255, 95)'
  }
  if(name == '*'){
    return 'lightgray'
  }
  if(name == 'Met'){
    return 'black'
  }
  return 'white'//coloring_aa(name)
}

console.log(ecoli_codon_to_amino_table)
draw_codon_usage_chart = function(dom_id, width, height, codon_usage){
  Sunburst()
    .data(codon_usage)     //.sort((a, b) => b.value - a.value)
    .label('name')
    .size('size')
    .width(width)
    .height(height)
    .color((d, parent) => coloring(d.name))
    .tooltipContent((d, node) => {
        console.log(node.depth)
        if(node.depth===3){
          codon = node.parent.parent.data.name + node.parent.data.name + node.data.name
          return `Amino Acid: ${ecoli_codon_to_amino_table[codon]}`
        }
        return ``
    })
    (document.getElementById(dom_id));
}

const codon_usage = {'F': {'TTC': 0.0, 'TTT': 1.0}, 'G': {'GGA': 0.0, 'GGC': 0.0, 'GGG': 1.0, 'GGT': 0.0}, 'I': {'ATA': 0.0, 'ATC': 0.0, 'ATT': 1.0}, 'K': {'AAA': 1.0, 'AAG': 0.0}, 'M': {'ATG': 1.0}, 'P': {'CCA': 0.0, 'CCC': 1.0, 'CCG': 0.0, 'CCT': 0.0}, 'W': {'TGG': 1.0}}
Object.keys(codon_usage).map(function(aa){
  codon_freq_dist = codon_usage[aa]
  Object.keys(codon_freq_dist).map(function(codon){

  })
})
draw_codon_usage_chart('codon_usage_chart', 1200, 600, json_data)


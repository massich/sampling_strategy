
@startuml
scale 800 width
abstract DataSimulationModel
DataSimulationModel : +generate_data (numSamples)
DataSimulationModel : +draw_model  (axisId)
DataSimulationModel ..> Plot
DataSimulationModel <|-- MultiVariatedGaussianModel
DataSimulationModel <|-- DoubleMVGM
DataSimulationModel <|-- HyperSpaceMVGM
HyperSpaceMVGM : -dimensions=3
HyperSpaceMVGM : +draw_model_3D  (axisId)    
    
DataSimulation "1" *-left- "2..*" DataSimulationModel
DataSimulation ..> Plot
DataSimulation : -randomSeed
DataSimulation : +numSamplesPerModel
DataSimulation : +modelsAndInfo
DataSimulation : +randomSets    
    
DataSimulation : +draw_samples (axisId)
    
DataSimulation   <|-right- DataSimulation_
DataSimulation_ : +numSamples    


abstract ProjectionModel
ProjectionModel : +project_data(data)
ProjectionModel : +display_base(axisId)
ProjectionModel ..> Plot   
ProjectionModel <|-- PCA
ProjectionModel <|-- SingleFeat
ProjectionModel <|-- LDA
abstract SamplingModel
SamplingModel <|-- ModeGaussian
SamplingModel <|-- Entropy

RandomSampler *-left- ProjectionModel
RandomSampler *-- SamplingModel
RandomSampler : -labelFlippingProb
RandomSampler : -noiseType
RandomSampler : -numSamples
RandomSampler : +labelModification
RandomSampler : +valueModification
RandomSampler : project_data(data)
RandomSampler : draw_sampling(axisId)
RandomSampler ..> Plot   

DataSimulation "0..*" -- "1..*" RandomSampler
(DataSimulation, RandomSampler) . Experiment
Experiment .left.> Plot   

@enduml  
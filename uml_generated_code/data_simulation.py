from object import *
from DataBaseCreator import *
from DataBase import *

class DataSimulation (object, DataBaseCreator):

    """
     Docstring for DataSimulation.
         This should be a subclass of a generic Data class.
     

    :version:
    :author: sik
    """

    def __init__(self, randomSeed):
        """
                 :randomSeed: TODO
         
         

        @param string randomSeed : 
        @return  :
        @author sik
        """
        pass

    def __str__(self):
        """
         

        @return string :
        @author sik
        """
        modelsInfoString="\t{0}_({1})_________________________\n\t\tmodel:: {2}\n \t\tsamples:: {3}\n \t\trange:: {4}\n"
        modelsInfo=""
        for d in self._data:
          modelsInfo+=modelsInfoString.format(
          d._class._name,d._class._color,d._model.get_model_information(),d._numOfSamples,d.get_range())
        return'Real-Data simulation ({0} Models):\n{1}'.format(
        len(self._data),modelsInfo)


    def get_range(self):
        """
         get_range returns the [xmin xmax ymin ymax] needed to display the
                 data
          I don't understand how to do this whithout numpy.

        @return string :
        @author sik
        """
        cBoundaries=np.asarray([c.get_range()for c in self._data])
        return[min(cBoundaries[:,0]),max(cBoundaries[:,1]),
        min(cBoundaries[:,2]),max(cBoundaries[:,3])]


    def get_all_data(self):
        """
         

        @return string :
        @author sik
        """
        return np.concatenate(
        list(d._samples for d in self._data),axis=0)
        


    def generate_default2MVGM_testcase(self):
        """
         Generate a 2 Multi-variated Gaussian class example
         

        @return DataBase :
        @author sik
        """
        np.random.seed(randomSeed)
        self._randomSeed=randomSeed
        classes=DataClasses()
        numSamplesPerModel=[n]*len(classes)
        MVGaussMod=MultiVariatedGaussianModel
        models=[MVGaussMod(0,1,1.2,1,0.8,dataClass=classes[0]),
        MVGaussMod(0,0,1.3,0.7,0.3,dataClass=classes[1])]buildParam=zip(classes,models,numSamplesPerModel)
        data=[]
        for currentClass,currentModel,nSamples in buildParam:
          data.append(
          DataContainer(dataClass=currentClass,dataModel=currentModel,dataSamples=currentModel.generate_data(nSamples)))
        
        self._data=data
        





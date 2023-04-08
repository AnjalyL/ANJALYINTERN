from django.db import models

# Create your models here.
class Listing(models.Model):
    Id = models.IntegerField(primary_key=True)
    MSSubClass = models.IntegerField()
    MSZoning  = models.IntegerField()
    LotFrontage = models.IntegerField(default=1)
    LotArea = models.IntegerField(default=1)
    Street = models.CharField(max_length=25, default="")
    Alley = models.CharField(max_length=25, default="")
    LotShape = models.CharField(max_length=25, default="")
    LandContour = models.CharField(max_length=25, default="")
    Utilities = models.CharField(max_length=25, default="")

    LotConfig = models.CharField(max_length=25 ,default="")
    LandSlope = models.CharField(max_length=25 ,default="")
    Neighborhood = models.CharField(max_length=25, default="")
    Condition1 = models.CharField(max_length=25, default="")
    Condition2 = models.CharField(max_length=25, default="")


    BldgType = models.CharField(max_length=25, default="")
    HouseStyle= models.CharField(max_length=25, default="")
    OverallQual= models.IntegerField( default=1)
    OverallCond= models.IntegerField(default=1)
    YearBuilt= models.IntegerField(default=1)
    YearRemodAdd= models.IntegerField(default=1)
    RoofStyle = models.CharField(max_length=25, default="")
    RoofMatl= models.CharField(max_length=25, default="")
    Exterior1st = models.CharField(max_length=25, default="")
    Exterior2nd= models.CharField(max_length=25, default="")
    MasVnrType= models.CharField(max_length=25, default="")

    MasVnrArea= models.IntegerField(default=1)
    ExterQual= models.CharField(max_length=25, default="")
    ExterCond= models.CharField(max_length=25, default="")
    Foundation= models.CharField(max_length=25, default="")
    BsmtQual= models.CharField(max_length=25, default="")
    BsmtCond= models.CharField(max_length=25, default="")
    BsmtExposure= models.CharField(max_length=25, default="")
    BsmtFinType1= models.CharField(max_length=25, default="")
    BsmtFinSF1= models.IntegerField(default=1)
    BsmtFinType2= models.CharField(max_length=25, default="")
    
    BsmtFinSF2= models.IntegerField(default=1)
    BsmtUnfSF= models.IntegerField(default=1)
    TotalBsmtSF= models.IntegerField(default=1)
    Heating= models.CharField(max_length=25, default="")
    HeatingQC= models.CharField(max_length=25, default="")
    CentralAir= models.CharField(max_length=25, default="")
    Electrical= models.CharField(max_length=25, default="")
    stFlrSF= models.IntegerField(default=1)
    ndFlrSF= models.IntegerField(default=1)
    LowQualFinSF= models.IntegerField(default=1)

    GrLivArea= models.IntegerField(default=1)
    BsmtFullBath= models.IntegerField(default=1)
    BsmtHalfBath= models.IntegerField(default=1)
    FullBath= models.IntegerField(default=1)
    HalfBath= models.IntegerField(default=1)
    BedroomAbvGr= models.IntegerField(default=1)
    KitchenAbvGr= models.IntegerField(default=1)
    KitchenQual= models.CharField(max_length=25, default="")
    TotRmsAbvGrd= models.IntegerField(default=1)
    Functional= models.CharField(max_length=25, default="") 

    Fireplaces= models.IntegerField(default=1)
    FireplaceQu= models.CharField(max_length=25, default="") 
    GarageType= models.CharField(max_length=25, default="") 
    GarageYrBlt= models.IntegerField(default=1)
    GarageFinish= models.CharField(max_length=25, default="") 
    GarageCars= models.IntegerField(default=1)
    GarageArea= models.IntegerField(default=1)
    GarageQual= models.CharField(max_length=25, default="") 
    GarageCond= models.CharField(max_length=25, default="") 
    PavedDrive= models.CharField(max_length=25, default="") 

    WoodDeckSF= models.IntegerField(default=1)
    OpenPorchSF= models.IntegerField(default=1)
    EnclosedPorch= models.IntegerField(default=1)
    SsnPorch= models.IntegerField(default=1)
    ScreenPorch= models.IntegerField(default=1)
    PoolArea= models.IntegerField(default=1)
    PoolQC= models.CharField(max_length=25, default="") 
    Fence = models.CharField(max_length=25, default="") 
    MiscFeature = models.CharField(max_length=25, default="") 


    MiscVal= models.IntegerField(default=1)
    MoSold= models.IntegerField(default=1)
    YrSold= models.IntegerField(default=1)
    SaleType= models.CharField(max_length=25, default="") 
    SaleCondition= models.CharField(max_length=25, default="") 
    SalePrice= models.IntegerField(default=1)

    def __str__(self):
        return self.Id
    

class booked(models.Model):
    SalePrice = models.ForeignKey(Listing,models.CASCADE)

    



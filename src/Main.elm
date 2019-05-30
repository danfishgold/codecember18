module Main exposing (main)

import Browser exposing (document)
import Browser.Events
import Element exposing (Element, column, el, height, px, text, width)
import Element.Font as Font
import Html exposing (Html)
import Task


main : Program WindowSize Model Msg
main =
    document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }



-- MODEL


type alias Model =
    { size : WindowSize }


type alias WindowSize =
    { width : Int, height : Int }


type Msg
    = SetSize WindowSize


type alias Day =
    { day : Int
    , title : String
    , description : String
    , content : VisualContent
    }


type VisualContent
    = Image String
    | Images (List String)
    | Video String



-- INIT


init : WindowSize -> ( Model, Cmd Msg )
init size =
    ( { size = size }, Cmd.none )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetSize size ->
            ( { size = size }, Cmd.none )



-- VIEW


view : Model -> Browser.Document Msg
view model =
    { title = ""
    , body = [ Element.layout [] (body model) ]
    }


type Layout
    = Wide
    | Narrow


body : Model -> Element Msg
body model =
    let
        layout =
            if toFloat model.size.width / toFloat model.size.height > 1.3 then
                Wide

            else
                Narrow
    in
    List.map (dayElement layout) days |> column [ Element.centerX ]


dayElement : Layout -> Day -> Element Msg
dayElement layout day =
    let
        title_ =
            dayTitle day.day day.title

        description_ =
            text day.description

        content =
            case day.content of
                Image src ->
                    image src

                Video src ->
                    image src

                Images (hd :: tl) ->
                    image hd

                Images [] ->
                    Element.none
    in
    case layout of
        Narrow ->
            Element.column []
                [ title_
                , description_
                , content
                ]

        Wide ->
            Element.row []
                [ content
                , Element.column []
                    [ title_
                    , description_
                    ]
                ]


dayTitle : Int -> String -> Element Msg
dayTitle day title_ =
    el [ Element.onLeft (title (String.fromInt day ++ ". ")) ] (title title_)


title : String -> Element Msg
title string =
    el [ Font.size 24, Font.bold ] (text string)


image : String -> Element Msg
image src =
    Element.image [ width (px 500), height (px 500) ]
        { src = src, description = "" }



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Browser.Events.onResize (\wd ht -> SetSize { width = wd, height = ht })



-- CONTENT


days : List Day
days =
    [ { day = 1
      , title = "Air Conditioner"
      , description = ""
      , content = Image "img/day_01.png"
      }
    , { day = 2
      , title = "Julia"
      , description = ""
      , content = Image "img/day_02.png"
      }
    , { day = 3
      , title = "Circles"
      , description = ""
      , content = Image "img/day_03.png"
      }
    , { day = 4
      , title = "Bouquet"
      , description = ""
      , content = Image "img/day_04.png"
      }
    , { day = 5
      , title = "Spirals"
      , description = ""
      , content = Video "img/day_05.mov"
      }
    , { day = 6
      , title = "Maze Complement"
      , description = ""
      , content = Image "img/day_06.png"
      }
    , { day = 7
      , title = "Pixels"
      , description = ""
      , content = Image "img/day_07.png"
      }
    , { day = 8
      , title = "Squares"
      , description = ""
      , content = Image "img/day_08.png"
      }
    , { day = 9
      , title = "Triangles"
      , description = ""
      , content = Image "img/day_09.png"
      }
    , { day = 10
      , title = "Tsuro"
      , description = ""
      , content = Image "img/day_10.png"
      }
    , { day = 11
      , title = "Blokus"
      , description = ""
      , content = Image "img/day_11.png"
      }
    , { day = 12
      , title = "Terrain"
      , description = ""
      , content = Image "img/day_12.png"
      }
    , { day = 13
      , title = "Topography"
      , description = ""
      , content = Image "img/day_13.png"
      }
    , { day = 14
      , title = "Pipes"
      , description = ""
      , content = Image "img/day_14.png"
      }
    , { day = 15
      , title = "Pattern"
      , description = ""
      , content =
            Images
                [ "img/day_15_1887.png"
                , "img/day_15_1538.png"
                , "img/day_15_3109.png"
                ]
      }
    , { day = 16
      , title = "Fave"
      , description = ""
      , content =
            Images
                [ "img/day_16_5.png"
                , "img/day_16_2255.png"
                , "img/day_16_5699.png"
                , "img/day_16_8385.png"
                ]
      }
    , { day = 17
      , title = "Sheaf"
      , description = ""
      , content = Video "img/day_17.mov"
      }
    , { day = 18
      , title = "Rays"
      , description = ""
      , content = Image "img/day_18.png"
      }
    , { day = 19
      , title = "Bar"
      , description = ""
      , content = Image "img/day_19.png"
      }
    , { day = 20
      , title = "Dashes"
      , description = ""
      , content = Image "img/day_20.png"
      }
    , { day = 21
      , title = "Carpet"
      , description = ""
      , content = Image "img/day_21.png"
      }
    , { day = 22
      , title = "Triangulation"
      , description = ""
      , content = Image "img/day_22.png"
      }
    , { day = 23
      , title = "Glass"
      , description = ""
      , content = Image "img/day_23.png"
      }
    , { day = 24
      , title = "Mountains"
      , description = ""
      , content = Image "img/day_24.png"
      }
    , { day = 25
      , title = "Cubes"
      , description = ""
      , content = Image "img/day_25.png"
      }
    , { day = 26
      , title = "Packing"
      , description = ""
      , content = Image "img/day_26.png"
      }
    , { day = 27
      , title = "Blocks"
      , description = ""
      , content = Image "img/day_27.png"
      }
    , { day = 28
      , title = "Glitch"
      , description = ""
      , content = Image "img/day_28.png"
      }
    , { day = 29
      , title = "Polygon Lines"
      , description = ""
      , content = Image "img/day_29.png"
      }
    , { day = 30
      , title = "Bye"
      , description = ""
      , content = Image "img/day_30.png"
      }
    ]
